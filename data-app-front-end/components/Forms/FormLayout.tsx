interface FormLayoutProps {
    title: string;
    children: React.ReactNode;
    onSubmit: (e: React.FormEvent<HTMLFormElement>) => void;
}

export default function FormLayout(
    {title, children, onSubmit} : FormLayoutProps) {
        return (
            <form onSubmit={onSubmit} className="max-w-md mx-auto bg-white p-8 rounded-lg shadow flex flex-col space-y-4">
                <h1 className="text-xl font-semibold mb-6">{title}</h1>
                {children}
            </form>
        );
    }