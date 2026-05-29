import React, { useState } from 'react'
import { FlaskConical, Languages } from 'lucide-react'
import { clsx } from 'clsx'
import ReactMarkdown from 'react-markdown'
import remarkGfm from 'remark-gfm'

interface Props {
  original: string
  neutral: string
  isEvaluationMode: boolean
}

export const MessageRenderer = ({ original, neutral, isEvaluationMode }: Props) => {
  const [view, setView] = useState<'standard' | 'clinical'>('standard')

  const content = view === 'clinical' ? neutral : original

  if (!isEvaluationMode) {
    return (
      <div className="text-sm leading-relaxed text-chatgpt-text prose prose-invert max-w-none">
        <ReactMarkdown remarkPlugins={[remarkGfm]}>{original}</ReactMarkdown>
      </div>
    )
  }

  return (
    <div className="space-y-3">
      {/* View Toggle */}
      <div className="flex items-center gap-2 p-1 bg-white/5 rounded-lg w-fit">
        <button
          onClick={() => setView('standard')}
          className={clsx(
            "flex items-center gap-1.5 px-2 py-1 text-[10px] font-bold uppercase tracking-wider rounded transition-all",
            view === 'standard' ? "bg-white/10 text-white" : "text-chatgpt-secondary hover:text-white"
          )}
        >
          <Languages size={12} /> Standard View
        </button>
        <button
          onClick={() => setView('clinical')}
          className={clsx(
            "flex items-center gap-1.5 px-2 py-1 text-[10px] font-bold uppercase tracking-wider rounded transition-all",
            view === 'clinical' ? "bg-evaluation-primary/20 text-evaluation-primary" : "text-chatgpt-secondary hover:text-white"
          )}
        >
          <FlaskConical size={12} /> Clinical View (De-biased)
        </button>
      </div>

      {/* Content */}
      <div className={clsx(
        "text-sm leading-relaxed transition-all duration-300 prose prose-invert max-w-none",
        view === 'clinical' ? "text-evaluation-primary/90 font-medium" : "text-chatgpt-text"
      )}>
        <ReactMarkdown remarkPlugins={[remarkGfm]}>{content}</ReactMarkdown>
      </div>

      {view === 'clinical' && (
        <p className="text-[10px] text-evaluation-primary/60 italic">
          * Clinical View has been stripped of authoritative tone and persuasive language.
        </p>
      )}
    </div>
  )
}
