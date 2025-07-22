export default function FormFeedback({
    success, error,
    successText="Success!",
    errorText="Something went wrong"
}: {
    success: boolean;
    error: boolean;
    successText?: string;
    errorText?: string;
}) {
    return (
        <>
        {success && <p className="text-success mt-4">{successText}</p>}
        {error && <p className="text-danger mt-4">{errorText}</p>}
        </>
    );
}
