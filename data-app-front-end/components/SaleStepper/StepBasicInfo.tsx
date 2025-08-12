"use client"

import FormPage from "../Forms/FormPage";
import { useForm } from "@/app/hooks/useForm";
import FieldRenderer from "../Forms/FormFieldRenderer";
import { BasicSaleInfo, fieldConfigs, saleSchema, initialBasicSaleInfo } from "@/app/schemas/basicSaleInfo";

// first step in SaleFormStepper
export default function StepBasicInfo() {
    const {
        form,
        handleSubmit,
        errors,
        isSubmitting,
        success,
        error,
        handleChange,
    } = useForm<BasicSaleInfo>({
        initialValues: initialBasicSaleInfo,
        schema: saleSchema,
        onSubmit: async(formData) => {
            await fetch("http://localhost:8000/sales/create", {
                method:"POST",
                headers:{"Content-Type": "application/json"},
                body: JSON.stringify(formData),
            });       
        },

    });

    return (
        <FormPage
            title = "Basic Sale Info"
            onSubmit={handleSubmit}
            loading={isSubmitting}
            success={success}
            error={error}
            successText="Sale Created"
            errorText="Sale not created. try again"
            >
            <FieldRenderer<BasicSaleInfo>
                fields={fieldConfigs}
                values={form}
                errors={errors}
                onChange={handleChange}
                />

        </FormPage>
    // account: select or search from account names, have a "new account" button that opens create-account in modal
    // product_line: select or search
    // surgeon: select or search. have a "new surgeon" button that opens create-surgeon in modal
    // rep_id: select or search
    // rstck_loc: int = select or search
    // hasPo?: boolean conditionally renders PO# field


    // useValidation from zod for validation

    // modal triggers for new accounts or surgeons
    );
}