import React from 'react'
import { HelpCircle } from 'lucide-react'

export const ReflectionPrompts = () => {
  const prompts = [
    "What specific part of this answer is most critical for my decision?",
    "If this AI were biased, what would it be trying to persuade me of?",
    "Do I have a primary source to confirm the key data points?"
  ]

  return (
    <div className="space-y-3">
      <h3 className="text-xs font-semibold uppercase tracking-wider text-chatgpt-secondary flex items-center gap-1.5 px-1">
        Self-Reflection Prompts <HelpCircle size={12} />
      </h3>
      
      <div className="grid gap-2">
        {prompts.map((p, i) => (
          <div key={i} className="p-3 bg-white/5 border border-white/10 rounded-xl hover:bg-white/10 transition-colors">
            <p className="text-xs text-chatgpt-secondary leading-relaxed">
              {p}
            </p>
          </div>
        ))}
      </div>
    </div>
  )
}
