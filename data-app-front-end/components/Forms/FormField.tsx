interface Props {
    label: string;
    name: string;
    value: string;
    onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
    type?: string;
    error?: string;
    helperText?: string;
}

export default function FormField({
    label,
    name,
    value,
    onChange,
    type = "text",
    error,
    helperText,
}: Props) {
    return(
        <div className="flex flex-col space-y-1">
            <label htmlFor={name} className="text-sm font-medium text-gray-700">
                {label}
            </label>
            <input
                id={name}
                name={name}
                value={value}
                onChange={onChange}
                type={type}
                className={`border rounded px-3 py-2 focus:outline-none focus:ring-2 ${
                    error ? "border-red-500 focus:ring-red-500" : "border-gray-300 focus:ring-blue-500"
                }`}
            />
            {helperText && !error && (
                <p className="text-xs text-gray-500">{helperText}</p>
            )}
            {error && (
                <p className="text-xs text-red-600">{error}</p>
            )}
        </div>
    );
}