import Link from "next/link";

export default function Sidebar() {
  return (
    <aside className="w-64 h-screen bg-gray-900 text-white flex flex-col">
      <div className="px-6 py-4 font-bold text-xl">📦 Data App</div>

      <nav className="flex flex-col space-y-2 px-6 mt-4">
        <Link href="/dashboard" className="hover:text-blue-400">Dashboard</Link>
        <Link href="/create-account" className="hover:text-blue-400">Create Account</Link>
        <Link href="/settings" className="hover:text-blue-400">Settings</Link>
      </nav>

      {/* Future: Avatar, Collapse Button, Theme Toggle */}
    </aside>
  );
}