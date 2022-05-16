from django.contrib.admin import AdminSite
from django.contrib import messages
from django.urls import path
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from sequences import get_next_value
from django.conf import settings
from django import forms
from .models.go_electric_rebate_application import GoElectricRebateApplication
from .services import cra


class UploadFileForm(forms.Form):
    cra_response_file = forms.FileField(
        help_text="Please upload the decoded CRA OUT file."
    )


class ITVRAdminSite(AdminSite):
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                "cra-download", self.admin_view(self.download_file), name="cra-download"
            ),
            path("cra-upload", self.admin_view(self.upload_file), name="cra-upload"),
        ]

        return custom_urls + urls

    # Create the filename for a CRA in file.
    # This needs to be named properly on the file before being encrypted.
    # '.p7m' is automatically added when the file is encrypted using Entrust.
    def get_cra_filename(self, program_code="BCVR", cra_env="A", cra_sequence="00001"):
        filename = "TO.{cra_env}TO#@@00.R7005.IN.{program_code}.{cra_env}{cra_sequence:05}".format(
            cra_env=cra_env, cra_sequence=cra_sequence, program_code=program_code
        )
        return filename

    def upload_file(self, request):
        if request.method == "POST":
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                file = request.FILES["cra_response_file"]
                file_contents = file.read()
                data = cra.read(file_contents)
                # TODO do something with this data
                # (store rebate amount receiving)
                print(data)
                messages.add_message(
                    request, messages.SUCCESS, "CRA OUT file uploaded successfully"
                )
                return HttpResponseRedirect("/admin")
        else:
            form = UploadFileForm()
        return render(request, "upload.html", {"form": form})

    def download_file(self, request):
        rebates = GoElectricRebateApplication.objects.filter(
            status=GoElectricRebateApplication.Status.VERIFIED
        )

        if rebates.count() == 0:
            response = HttpResponse("No income to check.")
            return response

        data = []
        cra_env = settings.CRA_ENVIRONMENT
        cra_sequence = get_next_value("cra_sequence")
        program_code = "BCVR"

        for rebate in rebates:
            data.append(
                {
                    "sin": rebate.sin,
                    "year": str(rebate.tax_year),  # should we just save as string?
                    "given_name": rebate.first_name,
                    "family_name": rebate.last_name,
                    "birth_date": rebate.date_of_birth.strftime("%Y-%m-%d"),
                }
            )

        filename = self.get_cra_filename(program_code, cra_env, cra_sequence)
        response = HttpResponse(
            cra.write(data, program_code, cra_env, f"{cra_sequence:05}"),
            content_type="text/plain",
        )
        response["Content-Disposition"] = "attachment; filename=" + filename
        return response

    # inline or attachment
