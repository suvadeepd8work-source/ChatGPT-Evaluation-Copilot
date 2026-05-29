import React, { useState, useEffect } from 'react'
import { useEvaluationStore } from '../store/evaluationStore'
import { ConfidenceIndicator } from './Evaluation/ConfidenceIndicator'
import { ToneTruthGauge } from './Evaluation/ToneTruthGauge'
import { BiasAlert } from './Evaluation/BiasAlert'
import { ClaimsList } from './Evaluation/ClaimsList'
import { VerificationChecklist } from './Evaluation/VerificationChecklist'
import { AccountabilityReminder } from './Evaluation/AccountabilityReminder'
import { ReflectionPrompts } from './Evaluation/ReflectionPrompts'
import { Shield, ChevronRight, Lock } from 'lucide-react'
import { DecisionSummary } from './DecisionSummary'

export const EvaluationPane = () => {
  const { isEvaluationMode, evaluationData, verifiedClaims } = useEvaluationStore()
  const [isFrictionLocked, setIsFrictionLocked] = useState(true)
  const [countdown, setCountdown] = useState(3)
  const [showSummary, setShowSummary] = useState(false)

  useEffect(() => {
    if (evaluationData && isEvaluationMode) {
      setShowSummary(false) // Reset summary when new data arrives
      setIsFrictionLocked(true)
      setCountdown(3)
      const timer = setInterval(() => {
        setCountdown(prev => {
          if (prev <= 1) {
            clearInterval(timer)
            setIsFrictionLocked(false)
            return 0
          }
          return prev - 1
        })
      }, 1000)
      return () => clearInterval(timer)
    }
  }, [evaluationData, isEvaluationMode])

  if (!isEvaluationMode) return null

  if (!evaluationData) {
    return (
      <div className="w-[450px] bg-evaluation-background border-l border-white/10 flex flex-col items-center justify-center p-8 text-center">
        <div className="text-white/20 mb-4">
          <Shield size={64} />
        </div>
        <h3 className="text-lg font-medium mb-2">Evidence Bench</h3>
        <p className="text-sm text-chatgpt-secondary">
          When you send a message in Evaluation Mode, the critical analysis will appear here.
        </p>
      </div>
    )
  }

  const { evaluation } = evaluationData
  const allClaimsVerified = verifiedClaims.length >= evaluation.claims.length

  if (showSummary) {
    return (
      <DecisionSummary 
        interactionId={evaluationData.interaction_id} 
        onBack={() => setShowSummary(false)} 
      />
    )
  }

  return (
    <div className="w-[450px] bg-evaluation-background border-l border-white/10 flex flex-col h-full overflow-hidden shadow-2xl z-20">
      {/* Header */}
      <div className="p-4 border-b border-white/10 bg-evaluation-background/80 backdrop-blur-md sticky top-0 z-10 flex items-center justify-between">
        <h2 className="text-sm font-bold flex items-center gap-2">
          <Shield size={16} className="text-evaluation-primary" />
          Evidence Bench
        </h2>
        <div className="text-[10px] px-2 py-1 rounded bg-white/10 text-chatgpt-secondary uppercase tracking-widest font-bold">
          {evaluationData.interaction_id.slice(0, 8)}
        </div>
      </div>

      {/* Content */}
      <div className="flex-1 overflow-y-auto p-4 space-y-6">
        <AccountabilityReminder 
          reminder={evaluation.accountability.reminder}
          required={evaluation.accountability.human_review_required}
        />

        <div className="grid grid-cols-1 gap-4">
          <ConfidenceIndicator 
            score={evaluation.confidence.score}
            reasoning={evaluation.confidence.reasoning}
          />
          <ToneTruthGauge 
            clinicalIndex={evaluation.tone.clinical_index}
            dominantTone={evaluation.tone.dominant_tone}
          />
        </div>

        <BiasAlert 
          score={evaluation.bias.bias_score}
          patterns={evaluation.bias.detected_patterns}
          recommendation={evaluation.bias.recommendation}
        />

        <ClaimsList claims={evaluation.claims} />

        <VerificationChecklist steps={evaluation.verification_steps} />

        <ReflectionPrompts />
      </div>

      {/* Footer / Friction Interaction */}
      <div className="p-4 border-t border-white/10 bg-evaluation-background/80 backdrop-blur-md">
        {isFrictionLocked ? (
          <button
            disabled
            className="w-full py-3 rounded-xl font-bold flex items-center justify-center gap-2 transition-all bg-white/5 text-chatgpt-secondary cursor-not-allowed"
          >
            <Lock size={16} /> Analyzing Evidence ({countdown}s)
          </button>
        ) : evaluation.accountability.human_review_required && !allClaimsVerified ? (
          <button
            disabled
            className="w-full py-3 rounded-xl font-bold flex items-center justify-center gap-2 transition-all bg-white/5 text-chatgpt-secondary cursor-not-allowed"
          >
            <Lock size={16} /> Verify all claims to proceed
          </button>
        ) : (
          <button
            onClick={() => setShowSummary(true)}
            className="w-full py-3 rounded-xl font-bold flex items-center justify-center gap-2 transition-all bg-evaluation-primary text-white hover:bg-evaluation-primary/90 shadow-lg shadow-evaluation-primary/20"
          >
            Confirm & Finalize Decision <ChevronRight size={18} />
          </button>
        )}
        <p className="text-[9px] text-center mt-3 text-chatgpt-secondary leading-relaxed">
          By clicking confirm, you acknowledge that you have reviewed the evidence and take full responsibility for any actions taken based on this AI-generated response.
        </p>
      </div>
    </div>
  )
}
