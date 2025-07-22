import { ZodObject, ZodRawShape } from "zod";

export interface FieldConfig {
    name: string;
    label: string;
    type: string;
    helperText?: string;
}

export function schemaCreate<T extends ZodRawShape>(schema:ZodObject<T>): FieldConfig[] {
    const shape = schema.shape;
    return Object.entries(shape).map(([name,def]) => {
        const type = def._def.typename;
        return {
            name,
            label: capitalize(name),
            type,
            helperText: generateHelperText(type, name),
        };
    });

}

function capitalize(str:string) {
    return str.charAt(0).toUpperCase() + str.slice(1);
}

function generateHelperText(type:string, name:string) {
    switch (type) {
        case "ZodString": 
            return `Enter ${name}`;
        case "ZodNumber":
            return `Provide a numeric value`;
        case "ZodBoolean":
            return `Toggle ${name}`;
        default:
            return `Enter ${name}`;
    }
}