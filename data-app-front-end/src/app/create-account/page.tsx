"use client";

import FormField from "../../../components/Forms/FormField";
import FormPage from "../../../components/Forms/FormPage";
import { useForm } from "../hooks/useForm";
import { schemaCreate } from "../../../lib/schemaCreate";
import FieldRenderer from "../../../components/Forms/FormFieldRenderer";

import { z } from "zod";

interface CreateAccountForm {
    name: string;
    address: string;
}

// create validation schema
const schema = z.object({
    name: z.string().min(2, "Name must be at least 2 characters"),
    address: z.string().min(5, "Address must be at least 5 characters")
})

export default function CreateAccountPage() {
    const {
        form,
        handleSubmit,
        errors,
        isSubmitting,
        success,
        error,
        handleChange,
    } = useForm<CreateAccountForm>({
        initialValues: {name:"", address:""},
        schema,
        onSubmit: async (formData) => {
            await fetch("http://localhost:8000/accounts/create", {
                method:"POST",
                headers:{"Content-Type": "application/json"},
                body: JSON.stringify(formData),
            });
        },
    });

    const fieldConfigs = schemaCreate(schema)

    return (
        <FormPage
            title="Create Account"
            onSubmit={handleSubmit}
            loading={isSubmitting}
            success={success}
            error={error}
            successText="Account Created Successfully"
            errorText="Accound Not Created. Try Again"
        >
            <FieldRenderer<CreateAccountForm> 
                fields={fieldConfigs}
                values={form}
                errors={errors}
                onChange={handleChange}
            />
        </FormPage>
    );
}