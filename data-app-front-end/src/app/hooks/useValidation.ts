import { ZodSchema } from "zod";

export function useValidation<T>(schema: ZodSchema<T>) {
  return (form: T) => {
    const result = schema.safeParse(form);
    if (!result.success) {
      const errors: Record<string, string> = {};
      for (const issue of result.error.issues) {
        errors[String(issue.path[0])] = issue.message;
      }
      return errors;
    }
    return {};
  };
}