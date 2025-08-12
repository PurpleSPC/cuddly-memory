import SaleFormStepper from "../../../components/SaleStepper/SaleFormStepper";
import { useSaleForm } from "../hooks/useSaleForm";
import PageLayout from "../../../components/Theme/PageLayout";
import { BasicSaleInfo } from "../schemas/basicSaleInfo";

export default function CreateSalePage(){
    const {
        step,
        setStep,
        saleId,
        submitBasicInfo,
        saleForm,
    } = useSaleForm<BasicSaleInfo>;

    return (
        <PageLayout>
            <h1 className="text-xl font-bold text-text">Create Sale</h1>

            <SaleFormStepper
                step={step}
                setStep = {setStep}
                saleID={saleID}
                onSubmitBasicInfo = {submitBasicInfo}
                saleForm = {saleForm}
            />

        </PageLayout>
    )
}

