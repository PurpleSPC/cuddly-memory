"use client";
import Link from "next/link";
import { useState } from "react";

export default function Sidebar() {
  const [collapsed, setCollapsed] = useState(false);

  return (
    <aside className={`h-screen bg-primary text-surface transition-all duration-300 ${collapsed ? "w-16" : "w-64"}`}>
      <div className="flex items-center justify-between px-4 py-4">
        {!collapsed && <span className="text-xl font-bold">PurpleSPaCe</span>}
        <button onClick={() => setCollapsed(!collapsed)} className="text-accent">
          {collapsed ? "expand" : "collapse"}
        </button>
      </div>

      <nav className="mt-4 space-y-4 px-4">
        <Link href="/dashboard" className="block text-surface hover:text-accent">
          {!collapsed ? "Dashboard" : "📊"}
        </Link>
        <Link href="/create-account" className="block text-surface hover:text-accent">
          {!collapsed ? "Create Account" : "➕"}
        </Link>
        <Link href="/settings" className="block text-surface hover:text-accent">
          {!collapsed ? "Settings" : "⚙️"}
        </Link>
      </nav>
    </aside>
  );
}