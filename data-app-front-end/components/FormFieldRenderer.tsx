import FormField from "./FormField";
import { FieldConfig } from "../lib/schemaCreate";


interface FieldRendererProps<T> {
    fields: FieldConfig[];
    values: T;
    errors: Partial<Record<keyof T,string>>;
    onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
}

export default function FieldRenderer<T>({ 
    fields, 
    values, 
    errors, 
    onChange,
} : FieldRendererProps<T>) {
    return (
        <>
        {fields.map((field) => (
            <FormField
                key={field.name}
                label={field.label}
                name={field.name}
                value={values[field.name as keyof T]}
                onChange={onChange}
                error={errors[field.name as keyof T]}
                helperText={field.helperText}
            />
        ))}
    </>
    );
}

