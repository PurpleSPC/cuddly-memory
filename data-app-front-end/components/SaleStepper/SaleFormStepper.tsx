import React from "react";
import { useState } from "react";



// handles the 3 step create-sale
// assigns each step a number and tracks the state
export default function SaleFormStepper() {
const [step, setStep] = useState(0);

const renderStep = () => {
    switch (step) {
        case 0: return <StepBasicInfo />;
        case 1: return <StepItems />;
        case 2: return <StepReview />;
    }
};

// shares form state with all steps


    return (
// handles next/back navigation

//  validate on next

// animated tranistions???

    )

}