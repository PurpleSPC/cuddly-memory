"use client";

import PageLayout from "../../../components/PageLayout";    

import { useState } from "react"

interface CreateAccountForm {
    name: string;
    address: string;
}

export default function CreateAccountPage() {
    const [form, setForm] = useState<CreateAccountForm>({
        name: "",
        address: "",
    });
    const [isSubmitting, setIsSubmitting] = useState(false);
    const [success, setSuccess] = useState(false);
    const [error, setError] = useState(false);
    
    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setForm({ ...form, [e.target.name]: e.target.value});
    };
    
    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setIsSubmitting(true);
        setSuccess(false);
        setError(false);
        
        try {
            const res = await fetch("http://localhost:8000/accounts/create", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(form),
        });
         if (res.ok) {
            setSuccess(true);
            setForm({name:"", address:""});
         } else {
            setError(true);
         }
        } catch {
            setError(true);
        } finally {
            setIsSubmitting(false);
        }

        console.log("Submitting ", form);
    }
    
    return (
        <PageLayout>
            <h1 className="text-2xl font-bold mb-6">Create Account</h1>
            <form className="flex flex-col space-y-4" onSubmit={handleSubmit}>
                <input 
                    className="border border-gray-300 rounded px-4 py-2 foucus:outline-none focus:ring-blue-500"
                    name="name" 
                    placeholder="Name" 
                    value={form.name} 
                    onChange={handleChange} />
                <input 
                    className="border border-gray-300 rounded px-4 py-2 foucus:outline-none focus:ring-blue-500"
                    name="address" 
                    placeholder="Address" 
                    value={form.address} 
                    onChange={handleChange} />
                <button 
                    className={`py-2 px-4 rounded text-white ${
                        isSubmitting? "bg-blue=300 cursor-not-allowed": "bg-blue-600 hover:bg-blue-700"
                    }`}
                    type="submit" 
                    disabled={isSubmitting}>
                    {isSubmitting ? "Creating..." : "Create Account"} 
                </button>
            </form>

            {/* Feedback Messages */}
            {success && <p className="text-green-600 mt-4">✅ Account created successfully!</p>}
            {error && <p className="text-red-600 mt-4">❌ Something went wrong. Try again.</p>}
        </PageLayout>
    );
}