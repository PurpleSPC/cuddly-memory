import React from "react";
import { useState } from "react";
import StepBasicInfo from "./StepBasicInfo";
import StepItems from "./StepItems";

// handles the 3 step create-sale
// assigns each step a number and tracks the state
export default function SaleFormStepper() {
const [step, setStep] = useState(0);

const renderStep = () => {
    switch (step) {
        case 0: return <StepBasicInfo />;
        case 1: return <StepItems />;
    }
};

// shares form state with all steps


    return (
        <div className="max-w-2xl mx-auto p-6 bg-surface shadow rounded">
            <h2 className=" text-xl font-semibold mb-4">Create Sale</h2>

            {/* step content */}
            <div className="mb-6">
                {renderStep()}
            </div>

            {/* nav butons */}
            <div className="flex justify-between">
                <button
                    onClick={() => setStep((prev) => Math.max(prev - 1, 0))}
                    disabled={step === 0}
                    className="px-4 py-2 bg-primary rounded hover:bg-accent"
                >
                    Next
                </button>
            </div>
    </div>
     );

}