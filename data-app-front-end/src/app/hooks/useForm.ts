import { useFormState } from "./useFormState";
import { useValidation } from "./useValidation";
import { useState } from "react";
import { z } from "zod"

export function useForm<T>({
  initialValues,
  schema,
  onSubmit,
}: {
  initialValues: T;
  schema: z.Schema<T>;
  onSubmit: (values: T) => Promise<void>;
}) {
  const { form, setForm, handleChange } = useFormState(initialValues);
  const validate = useValidation(schema);

  const [errors, setErrors] = useState<Record<string, string>>({});
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [success, setSuccess] = useState(false);
  const [error, setError] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    await submitForm();
  };

  const submitForm = async () => {
    const formErrors = validate(form);
    if (Object.keys(formErrors).length) {
      setErrors(formErrors);
      return;
    }
    setErrors({});
    setIsSubmitting(true);
    setSuccess(false);
    setError(false);

    try {
      await onSubmit(form);
      setSuccess(true);
      setForm(initialValues); // reset form
    } catch {
      setError(true);
    } finally {
      setIsSubmitting(false);
    }
  };

  return {
    form,
    handleChange,
    handleSubmit,
    submitForm,
    isSubmitting,
    success,
    error,
    errors,
  };
}