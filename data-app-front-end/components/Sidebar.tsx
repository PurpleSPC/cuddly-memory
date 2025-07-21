import Link from "next/link";

export default function Sidebar() {
  return (
    <aside className="w-64 h-screen bg-primary text-text flex flex-col">
      <div className="px-6 py-4 font-bold text-xl">📦 Data App</div>

      <nav className="flex flex-col space-y-2 px-6 mt-4">
        <Link href="/dashboard" className="hover:text-accent">Dashboard</Link>
        <Link href="/create-account" className="hover:text-accent">Create Account</Link>
        <Link href="/settings" className="hover:text-accent">Settings</Link>
      </nav>

      {/* Future: Avatar, Collapse Button, Theme Toggle */}
    </aside>
  );
}