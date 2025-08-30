"use client"

import SaleFormStepper from "../../../components/SaleStepper/SaleFormStepper";
import { useSaleForm } from "../hooks/useSaleForm";
import PageLayout from "../../../components/Theme/PageLayout";
import { BasicSaleInfo } from "../schemas/basicSaleInfo";

export default function CreateSalePage(){
    const {
        step,
        setStep,
        saleID,
        basicInfoForm,
    } = useSaleForm();

    const handleSubmitBasicInfo = async () => {
        try {
            await basicInfoForm.submitForm();
        } catch (error) {
            console.error("Failed to submit basic info:", error);
        }
    };

    return (
        <PageLayout>
            <h1 className="text-xl font-bold text-text">Create Sale</h1>

            <SaleFormStepper
                step={step}
                setStep={setStep}
                saleID={saleID}
                onSubmitBasicInfo={handleSubmitBasicInfo}
                saleForm={basicInfoForm}
            />
        </PageLayout>
    );
}

