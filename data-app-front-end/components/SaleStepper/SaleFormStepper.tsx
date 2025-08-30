"use client"

import React from "react";
import StepBasicInfo from "./StepBasicInfo";
import StepItems from "./StepItems";
import StepReview from "./StepReview";
import { BasicSaleInfo } from "@/app/schemas/basicSaleInfo";

interface SaleFormStepperProps {
    step: number;
    setStep: (step: number) => void;
    saleID: number | null;
    onSubmitBasicInfo: (data: BasicSaleInfo) => Promise<void>;
    saleForm: {
        form: BasicSaleInfo;
        handleSubmit: (e: React.FormEvent) => Promise<void>;
        errors: Record<string, string>;
        isSubmitting: boolean;
        success: boolean;
        error: boolean;
        handleChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
    };
}

// handles the 3 step create-sale
// assigns each step a number and tracks the state
export default function SaleFormStepper({ step, setStep, saleID, onSubmitBasicInfo, saleForm }: SaleFormStepperProps) {
    const steps = [
        { id: 0, title: "Basic Info", description: "Enter sale details" },
        { id: 1, title: "Sale Items", description: "Add products to sale" },
        { id: 2, title: "Review & Submit", description: "Review and finalize" }
    ];

    const renderStep = () => {
        switch (step) {
            case 0: 
                return <StepBasicInfo onSubmitBasicInfo={onSubmitBasicInfo} saleForm={saleForm} />;
            case 1: 
                return <StepItems saleID={saleID} />;
            case 2: 
                return <StepReview saleID={saleID} />;
            default: 
                return <StepBasicInfo onSubmitBasicInfo={onSubmitBasicInfo} saleForm={saleForm} />;
        }
    };

    const canGoNext = () => {
        if (step === 0) return saleID !== null; // Can only proceed after basic info is saved
        if (step === 1) return true; // Can always proceed to review
        return false; // Can't proceed from review
    };

    const canGoPrev = () => step > 0;

    const nextStep = () => {
        if (canGoNext()) {
            setStep(step + 1);
        }
    };

    const prevStep = () => {
        if (canGoPrev()) {
            setStep(step - 1);
        }
    };

    return (
        <div className="max-w-4xl mx-auto p-6 bg-surface shadow rounded">
            <h2 className="text-2xl font-semibold mb-6 text-center">Create Sale</h2>

            {/* Step Indicators */}
            <div className="mb-8">
                <div className="flex items-center justify-between">
                    {steps.map((stepItem, index) => (
                        <React.Fragment key={stepItem.id}>
                            <div className="flex flex-col items-center">
                                <div className={`w-10 h-10 rounded-full flex items-center justify-center text-sm font-medium ${
                                    step >= stepItem.id 
                                        ? 'bg-primary text-white' 
                                        : 'bg-gray-200 text-gray-600'
                                }`}>
                                    {step > stepItem.id ? '✓' : stepItem.id + 1}
                                </div>
                                <div className="mt-2 text-center">
                                    <div className={`text-sm font-medium ${
                                        step >= stepItem.id ? 'text-primary' : 'text-gray-500'
                                    }`}>
                                        {stepItem.title}
                                    </div>
                                    <div className="text-xs text-gray-400 mt-1">
                                        {stepItem.description}
                                    </div>
                                </div>
                            </div>
                            {index < steps.length - 1 && (
                                <div className={`flex-1 h-0.5 mx-4 ${
                                    step > stepItem.id ? 'bg-primary' : 'bg-gray-200'
                                }`} />
                            )}
                        </React.Fragment>
                    ))}
                </div>
            </div>

            {/* Step Content */}
            <div className="mb-8 min-h-[400px]">
                {renderStep()}
            </div>

            {/* Navigation Buttons */}
            <div className="flex justify-between">
                <button
                    onClick={prevStep}
                    disabled={!canGoPrev()}
                    className={`px-6 py-2 rounded-lg font-medium transition-colors ${
                        canGoPrev()
                            ? 'bg-gray-200 text-gray-800 hover:bg-gray-300'
                            : 'bg-gray-100 text-gray-400 cursor-not-allowed'
                    }`}
                >
                    Previous
                </button>
                
                <div className="flex gap-3">
                    {step < 2 && (
                        <button
                            onClick={nextStep}
                            disabled={!canGoNext()}
                            className={`px-6 py-2 rounded-lg font-medium transition-colors ${
                                canGoNext()
                                    ? 'bg-primary text-white hover:bg-accent'
                                    : 'bg-gray-200 text-gray-400 cursor-not-allowed'
                            }`}
                        >
                            {step === 1 ? 'Review & Submit' : 'Next'}
                        </button>
                    )}
                </div>
            </div>
        </div>
    );
}