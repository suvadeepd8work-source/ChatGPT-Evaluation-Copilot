import React, { ReactNode } from 'react'

interface LayoutProps {
  children?: ReactNode
}

export const Layout = ({ children }: LayoutProps) => {
  return (
    <div className="flex h-screen w-full bg-chatgpt-gray overflow-hidden">
      {/* Sidebar - Placeholder */}
      <div className="w-64 bg-chatgpt-sidebar flex flex-col hidden md:flex">
        <div className="p-4 flex items-center justify-between">
          <button className="flex items-center gap-3 w-full p-3 text-sm rounded-md border border-white/20 hover:bg-white/5 transition-colors">
            <span className="text-xl">+</span> New Chat
          </button>
        </div>
        <div className="flex-1 overflow-y-auto p-2">
          {/* Recent chats placeholder */}
        </div>
        <div className="p-4 border-t border-white/10 text-xs text-chatgpt-secondary">
          Phase 4: Evaluation Mode Prototype
        </div>
      </div>

      {/* Main Content */}
      <main className="flex-1 flex flex-col h-full overflow-hidden relative">
        {children}
      </main>
    </div>
  )
}
