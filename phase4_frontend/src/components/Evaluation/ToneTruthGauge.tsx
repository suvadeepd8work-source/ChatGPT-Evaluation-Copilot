import React from 'react'
import { Activity } from 'lucide-react'

interface Props {
  clinicalIndex: number
  dominantTone: string
}

export const ToneTruthGauge = ({ clinicalIndex, dominantTone }: Props) => {
  const truthPercentage = Math.round(clinicalIndex * 100)
  const tonePercentage = 100 - truthPercentage

  return (
    <div className="bg-white/5 rounded-xl p-4 border border-white/10">
      <h3 className="text-xs font-semibold uppercase tracking-wider text-chatgpt-secondary flex items-center gap-1.5 mb-4">
        Tone vs Truth <Activity size={12} />
      </h3>
      
      <div className="flex items-center gap-4 mb-2">
        <div className="flex-1 flex flex-col items-center">
          <span className="text-xs text-chatgpt-secondary mb-1">Truth (Clinical)</span>
          <div className="w-full bg-white/10 h-16 rounded-lg relative overflow-hidden flex items-end">
            <div 
              className="w-full bg-evaluation-info/40 transition-all duration-700"
              style={{ height: `${truthPercentage}%` }}
            />
            <span className="absolute inset-0 flex items-center justify-center font-bold text-sm">
              {truthPercentage}%
            </span>
          </div>
        </div>
        
        <div className="flex-1 flex flex-col items-center">
          <span className="text-xs text-chatgpt-secondary mb-1">Tone ({dominantTone})</span>
          <div className="w-full bg-white/10 h-16 rounded-lg relative overflow-hidden flex items-end">
            <div 
              className="w-full bg-evaluation-warning/40 transition-all duration-700"
              style={{ height: `${tonePercentage}%` }}
            />
            <span className="absolute inset-0 flex items-center justify-center font-bold text-sm">
              {tonePercentage}%
            </span>
          </div>
        </div>
      </div>
      
      <p className="text-[10px] text-center text-chatgpt-secondary mt-2">
        Higher "Truth" indicates a clinical, evidence-based response.
      </p>
    </div>
  )
}
