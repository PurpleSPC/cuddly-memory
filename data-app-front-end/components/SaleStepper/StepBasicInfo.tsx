"use client"

import FormPage from "../Forms/FormPage";
import { useForm } from "@/app/hooks/useForm";
import FieldRenderer from "../Forms/FormFieldRenderer";
import { BasicSaleInfo, fieldConfigs, saleSchema, initialBasicSaleInfo } from "@/app/schemas/basicSaleInfo";

interface StepBasicInfoProps {
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

// first step in SaleFormStepper
export default function StepBasicInfo({ onSubmitBasicInfo }: StepBasicInfoProps) {
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
            await onSubmitBasicInfo(formData);
        },
    });

    return (
        <FormPage
            title="Basic Sale Info"
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
    );
}