/* eslint-disable react/jsx-indent */
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import React from 'react';

const EligibilityPage = (props) => {
  const {
    handleInputChange, handleSubmit,
  } = props;
  return (
    <div>
      <div>

        <h1>Electric Vehicle Rebates</h1>
        <h2>for Individuals and Households</h2>
      </div>
      <div>
        <p>
          Rebates of up to $4,000 are available from the B.C. Government towards the purchase of a
          new electric vehicle. Your individual or household income determines the rebate amount.
        </p>
        <h3>How it works</h3>
        <div>
          <ol>
            <li>Complete the following eligibility questions and online application process.</li>
            <li>
              If you are eligible, a rebate code will be emailed to you that indicates
              your rebate amount.

            </li>
            <li>
              The rebate code is associated with your B.C. Driver&apos;s Licence number.
              They are both needed at the car dealership to receive the rebate discount at the
              time of vehicle purchase.
            </li>
          </ol>
        </div>
        <h4>Rebate Application Type (Individual or Household)</h4>
        <p>
          If your total individual income was $100,000 or less or your total household income was
          $165,000 or less you are eligible for a rebate at the following rates:
        </p>
        <table>
          <tbody>
            <tr>
              <th>Individual Income</th>
              <th>Household Income</th>
              <th>
                Rebate Amount Range
                <sup>1</sup>
              </th>
            </tr>
            <tr>
              <td>Less than $80,000</td>
              <td>Less than $125,000</td>
              <td>$2,000 - $4,000</td>
            </tr>
            <tr>
              <td>$80,001 - 90,000</td>
              <td>$125,001 - 145,000</td>
              <td>$1,000 - $2,000</td>
            </tr>
            <tr>
              <td>$90,001 - 100,000</td>
              <td>$145,001 - 165,000</td>
              <td>$500 - $1,000</td>
            </tr>
          </tbody>
        </table>
        <sup>1</sup>
        <sub>
          BEV (Battery Electric Vehicle) and long-range PHEV (Plug-in Hybrid Electric Vehicle)
          receive the higher rebate amount.
        </sub>
        <p>
          Your income will be verified with the Canada Revenue Agency based on your
          2020*
          notice of assessment (line 15000).
        </p>
        <h3>
        Determine your eligibility for a rebate
        </h3>
      </div>
    </div>
  );
};

export default EligibilityPage;