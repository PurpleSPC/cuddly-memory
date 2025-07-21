import { ReactNode } from "react";

type Props = {
    loading: boolean;
    children: ReactNode;
    className?: string;
    type?: "button" | "submit";
    disabled?: boolean;
};

export default function SubmitButton({
    loading, 
    children,
    className="",
    type = "submit",
    disabled = false,
}: Props) {
    return (
        <button
            type={type}
            disabled={disabled || loading}
            className={`py-2 px-4 rounded text-text transition ${
                loading ? "bg-muted cursor-not-allowed" : "bg-primary hover:bg-accent"
            } ${className}`}
        >
            {loading ? "Submitting..." : children}
        </button>
    );
}
