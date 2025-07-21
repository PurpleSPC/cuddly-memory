import Sidebar from "./Sidebar";



// min-h-screen = ensures full height
// bg-gray-50 = light gray background
// max-3xl mx-auto = centers with a max width
// p-6 = adds padding
export default function PageLayout({children} : {children: React.ReactNode}) {
    return (
        <div className="flex">
            <Sidebar/>
            <main className="flex-1 bg-background p-6">
                {children}
            </main>
        </div>
    );
}