import React from 'react'
import { Info } from 'lucide-react'

interface Props {
  score: number
  reasoning: string
}

export const ConfidenceIndicator = ({ score, reasoning }: Props) => {
  const percentage = Math.round(score * 100)
  
  const getColor = () => {
    if (score > 0.8) return 'bg-evaluation-primary'
    if (score > 0.5) return 'bg-evaluation-warning'
    return 'bg-evaluation-error'
  }

  return (
    <div className="bg-white/5 rounded-xl p-4 border border-white/10">
      <div className="flex items-center justify-between mb-3">
        <h3 className="text-xs font-semibold uppercase tracking-wider text-chatgpt-secondary flex items-center gap-1.5">
          Confidence Score <Info size={12} className="cursor-help" />
        </h3>
        <span className={`text-lg font-bold ${score > 0.8 ? 'text-evaluation-primary' : score > 0.5 ? 'text-evaluation-warning' : 'text-evaluation-error'}`}>
          {percentage}%
        </span>
      </div>
      
      <div className="w-full bg-white/10 h-2 rounded-full overflow-hidden mb-3">
        <div 
          className={`h-full transition-all duration-1000 ease-out ${getColor()}`}
          style={{ width: `${percentage}%` }}
        />
      </div>
      
      <p className="text-[11px] leading-relaxed text-chatgpt-secondary italic">
        "{reasoning}"
      </p>
    </div>
  )
}
