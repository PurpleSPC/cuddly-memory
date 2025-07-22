"use client";
import PageLayout from "./PageLayout";
import FormLayout from "./FormLayout";
import SubmitButton from "./SubmitButton";
import FormFeedback from "./FeedbackMessage";

interface FormPageProps {
  title: string;
  onSubmit: (e: React.FormEvent) => void;
  children: React.ReactNode;
  loading?: boolean;
  success?: boolean;
  error?: boolean;
  successText?: string;
  errorText?: string;
}

export default function FormPage({
  title,
  onSubmit,
  children,
  loading = false,
  success = false,
  error = false,
  successText = "Success!",
  errorText = "Something went wrong.",
}: FormPageProps) {
  return (
    <PageLayout>
      <h1 className="text-2xl font-bold mb-6 mx-auto">{title}</h1>
      <FormLayout title={title} onSubmit={onSubmit}>
        {children}
        <SubmitButton loading={loading} className="mt-4">
          {title}
        </SubmitButton>
      </FormLayout>
      <FormFeedback success={success} error={error} successText={successText} errorText={errorText} />
    </PageLayout>
  );
}