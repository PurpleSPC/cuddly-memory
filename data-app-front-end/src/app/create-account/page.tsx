"use client";

import PageLayout from "../../../components/PageLayout";    
import FormLayout from "../../../components/FormLayout";
import SubmitButton from "../../../components/SubmitButton";
import FormField from "../../../components/FormField";

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
    const [form, setForm] = useState<CreateAccountForm>({
        name: "",
        address: "",
    });
    const [isSubmitting, setIsSubmitting] = useState(false);
    const [success, setSuccess] = useState(false);
    const [errors, setErrors] = useState<{ [key:string]: string}>({}); // uses formErrors from validation function
    const [error, setError] = useState(false);

    
    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setForm({ ...form, [e.target.name]: e.target.value});
    };
    
    // Validation function from schema
    const validateForm = () => {
        const result = createAccountSchema.safeParse(form);
        if (!result.success) {
            const formErrors : Record<string, string> = {};
            for (const issue of result.error.issues) {
                formErrors[String(issue.path[0])] = issue.message;
            }
            return formErrors;
        }
        return {};
    };

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        const formErrors = validateForm();
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
        <PageLayout>
            <h1 className="text-2xl font-bold mb-6 mx-auto">Create Account</h1>
            <FormLayout title="Create Account" onSubmit={handleSubmit}>
                <FormField 
                    label="name" 
                    name="name" 
                    value={form.name} 
                    onChange={handleChange}
                    error={errors.name}
                    helperText="Enter Account Name"    
                />
                <FormField 
                    label="address" 
                    name="address" 
                    value={form.address} 
                    onChange={handleChange} 
                    error={errors.name}
                    helperText="Enter account address"
                />
                <SubmitButton loading={isSubmitting} className="mt-4">
                    Create Account
                </SubmitButton>
            </FormLayout>

            {/* Feedback Messages */}
            {success && <p className="text-green-600 mt-4">Account created successfully!</p>}
            {error && <p className="text-red-600 mt-4">Something went wrong. Try again.</p>}
        </PageLayout>
    );
}