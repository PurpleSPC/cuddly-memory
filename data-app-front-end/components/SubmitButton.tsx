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
            className={`py-2 px-4 rounded text-white transition ${
                loading ? "bg-blue-300 cursor-not-allowed" : "bg-blue-600 hover:bg-blue-700"
            } ${className}`}
        >
            {loading ? "Submitting..." : children}
        </button>
    );
}
