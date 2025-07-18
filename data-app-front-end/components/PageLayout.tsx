// min-h-screen = ensures full height
// bg-gray-50 = light gray background
// max-3xl mx-auto = centers with a max width
// p-6 = adds padding


export default function PageLayout({children} : {children: React.ReactNode}) {
    return (
        <main className="min-h-screen bg-gray-50">
            <div className="max-w-3xl mx-auto p-6">
                {children}
            </div>
        </main>
    );
}