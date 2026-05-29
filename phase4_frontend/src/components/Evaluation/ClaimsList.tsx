import React from 'react'
import { FileText, CheckCircle2, Circle } from 'lucide-react'
import { useEvaluationStore } from '../../store/evaluationStore'

interface Props {
  claims: string[]
}

export const ClaimsList = ({ claims }: Props) => {
  const { verifiedClaims, toggleClaimVerification } = useEvaluationStore()

  return (
    <div className="space-y-3">
      <h3 className="text-xs font-semibold uppercase tracking-wider text-chatgpt-secondary flex items-center gap-1.5 px-1">
        Claims Decomposition <FileText size={12} />
      </h3>
      
      <div className="space-y-2">
        {claims.map((claim, index) => {
          const isVerified = verifiedClaims.includes(claim)
          return (
            <div 
              key={index}
              onClick={() => toggleClaimVerification(claim)}
              className={`p-3 rounded-xl border transition-all cursor-pointer group ${
                isVerified 
                  ? 'bg-evaluation-primary/10 border-evaluation-primary/30' 
                  : 'bg-white/5 border-white/10 hover:border-white/20'
              }`}
            >
              <div className="flex items-start gap-3">
                <div className={`mt-0.5 transition-colors ${isVerified ? 'text-evaluation-primary' : 'text-chatgpt-secondary group-hover:text-white'}`}>
                  {isVerified ? <CheckCircle2 size={16} /> : <Circle size={16} />}
                </div>
                <p className={`text-xs leading-relaxed ${isVerified ? 'text-white' : 'text-chatgpt-text/80'}`}>
                  {claim}
                </p>
              </div>
            </div>
          )
        })}
      </div>
    </div>
  )
}
