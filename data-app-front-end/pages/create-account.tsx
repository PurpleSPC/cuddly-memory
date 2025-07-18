"use client";

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
        <main>
            <h1>Create Account</h1>
            <form onSubmit={handleSubmit}>
                <input name="name" placeholder="Name" value={form.name} onChange={handleChange} />
                <input name="address" placeholder="Address" value={form.address} onChange={handleChange} />
                <button type="submit" disabled={isSubmitting}>
                    {isSubmitting ? "Creating..." : "Create Account"} 
                </button>
            </form>
            {/* Feedback Messages */}
            {success && <p style={{color: "green"}}>✅ Account created successfully!</p>}
            {error && <p style={{color:"red"}}>❌ Something went wrong. Try again.</p>}
        </main>
    );
}