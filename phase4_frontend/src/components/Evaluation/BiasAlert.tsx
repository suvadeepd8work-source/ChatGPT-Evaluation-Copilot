import React from 'react'
import { AlertTriangle } from 'lucide-react'

interface Props {
  score: number
  patterns: string[]
  recommendation: string
}

export const BiasAlert = ({ score, patterns, recommendation }: Props) => {
  if (score < 0.2) return null

  return (
    <div className="bg-evaluation-warning/10 rounded-xl p-4 border border-evaluation-warning/20">
      <div className="flex items-start gap-3">
        <div className="text-evaluation-warning mt-0.5">
          <AlertTriangle size={18} />
        </div>
        <div>
          <h3 className="text-sm font-bold text-evaluation-warning mb-1">
            Bias Detected
          </h3>
          <p className="text-xs text-chatgpt-text/80 mb-3">
            The AI is using persuasive or authoritative language that may influence your judgment.
          </p>
          
          <div className="flex flex-wrap gap-2 mb-3">
            {patterns.map((p, i) => (
              <span key={i} className="text-[10px] px-2 py-0.5 bg-evaluation-warning/20 rounded-full text-evaluation-warning border border-evaluation-warning/30">
                "{p}"
              </span>
            ))}
          </div>
          
          <p className="text-[11px] text-chatgpt-secondary italic">
            <strong>Recommendation:</strong> {recommendation}
          </p>
        </div>
      </div>
    </div>
  )
}
