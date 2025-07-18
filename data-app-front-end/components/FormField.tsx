interface Props {
    label: string;
    name: string;
    value: string;
    onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
    type?: string;
}

export default function FormField({
    label,
    name,
    value,
    onChange,
    type = "text"
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
                className="border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus: ring-blue-500"
            />
        </div>
    );
}