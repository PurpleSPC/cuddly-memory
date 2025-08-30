import { ZodObject, ZodRawShape } from "zod";

export interface FieldConfig {
    name: string;
    label: string;
    type: string;
    helperText?: string;
}

export function schemaCreate<T extends ZodRawShape>(schema: ZodObject<T>): FieldConfig[] {
    const shape = schema.shape;
    return Object.entries(shape).map(([name]) => {
        // Simple type detection based on common patterns
        const type = detectInputType(name);
        return {
            name,
            label: capitalize(name),
            type,
            helperText: generateHelperText(type, name),
        };
    });
}

function detectInputType(fieldName: string): string {
    // Simple heuristic-based type detection
    const lowerName = fieldName.toLowerCase();
    
    if (lowerName.includes('date')) return 'date';
    if (lowerName.includes('id')) return 'number';
    if (lowerName.includes('price') || lowerName.includes('cost')) return 'number';
    if (lowerName.includes('qty') || lowerName.includes('quantity')) return 'number';
    if (lowerName.includes('email')) return 'email';
    if (lowerName.includes('phone')) return 'tel';
    if (lowerName.includes('url')) return 'url';
    
    // Default to text for most fields
    return 'text';
}

function capitalize(str: string) {
    return str.charAt(0).toUpperCase() + str.slice(1);
}

function generateHelperText(type: string, name: string) {
    switch (type) {
        case "date": 
            return `Select ${name}`;
        case "number":
            return `Enter ${name}`;
        case "email":
            return `Enter email address`;
        case "tel":
            return `Enter phone number`;
        case "url":
            return `Enter URL`;
        default:
            return `Enter ${name}`;
    }
}