"use client";

import FormField from "../../../components/FormField";
import { useFormState } from "../hooks/useFormState";
import { useValidation } from "../hooks/useValidation";
import FormPage from "../../../components/FormPage";

import { useState } from "react"

import { z } from "zod";

interface CreateAccountForm {
    name: string;
    address: string;
}

// create validation schema
const createAccountSchema = z.object({
    name: z.string().min(2, "Name must be at least 2 characters"),
    address: z.string().min(5, "Address must be at least 5 characters")
})

export default function CreateAccountPage() {
    const {form, setForm, handleChange} = useFormState({
        name: "",
        address: "",
    });
    const [isSubmitting, setIsSubmitting] = useState(false);
    const [success, setSuccess] = useState(false);
    const [errors, setErrors] = useState<Record<string, string>>({}); 
    const [error, setError] = useState(false);

    const validate = useValidation(createAccountSchema)
    
    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        const formErrors = validate(form);
        if (Object.keys(formErrors).length > 0) {
            setErrors(formErrors);
            return;
        }
        setErrors({});
        setIsSubmitting(true);
        setSuccess(false);
        setError(false);
        
        try {
            const res = await fetch("http://localhost:8000/accounts/create", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(form),
        });

        if (!res.ok) throw new Error("Request failed");

        setSuccess(true);
        setForm({ name: "", address: ""});
        } catch {
            setError(true);
        } finally {
            setIsSubmitting(false);
        }
    }
    
    return (
        <FormPage
        title="Create Account"
        onSubmit={handleSubmit}
        loading={isSubmitting}
        success={success}
        error={error}
        successText="Account Created Successfully!"
        errorText="Something went wrong. Try again"
        >
            <FormField 
                label="Name" 
                name="name" 
                value={form.name} 
                onChange={handleChange}
                error={errors.name}
                helperText="Enter Account Name"    
            />
            <FormField 
                label="Address" 
                name="address" 
                value={form.address} 
                onChange={handleChange} 
                error={errors.name}
                helperText="Enter account address"
            />
        </FormPage>
    );
}