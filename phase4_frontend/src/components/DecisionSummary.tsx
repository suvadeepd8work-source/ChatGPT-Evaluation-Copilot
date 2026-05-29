import React from 'react'
import { CheckCircle, ShieldCheck, FileText, AlertTriangle, ArrowLeft } from 'lucide-react'

interface Props {
  interactionId: string
  onBack: () => void
}

export const DecisionSummary = ({ interactionId, onBack }: Props) => {
  return (
    <div className="fixed inset-0 z-50 bg-chatgpt-gray flex items-center justify-center p-4">
      <div className="max-w-2xl w-full bg-evaluation-background border border-white/10 rounded-2xl shadow-2xl overflow-hidden flex flex-col max-h-[90vh]">
        {/* Header */}
        <div className="p-6 border-b border-white/10 bg-evaluation-primary/10 flex items-center gap-4">
          <div className="p-3 bg-evaluation-primary/20 rounded-full text-evaluation-primary">
            <CheckCircle size={32} />
          </div>
          <div>
            <h1 className="text-2xl font-bold text-white">Decision Finalized</h1>
            <p className="text-chatgpt-secondary text-sm">Interaction Audit ID: {interactionId}</p>
          </div>
        </div>

        {/* Content */}
        <div className="flex-1 overflow-y-auto p-8 space-y-8">
          <section className="space-y-4">
            <h2 className="text-lg font-semibold flex items-center gap-2">
              <ShieldCheck size={20} className="text-evaluation-primary" />
              Human Accountability Log
            </h2>
            <div className="bg-white/5 rounded-xl p-4 border border-white/10">
              <p className="text-sm text-chatgpt-text leading-relaxed">
                You have officially signed off on this AI-generated response. This interaction has been logged with your verification status as <strong>"Manually Audited"</strong>.
              </p>
            </div>
          </section>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div className="bg-white/5 rounded-xl p-4 border border-white/10 space-y-2">
              <h3 className="text-xs font-bold uppercase tracking-wider text-chatgpt-secondary flex items-center gap-2">
                <FileText size={14} /> Audit Trail
              </h3>
              <p className="text-sm text-white">Full claim decomposition and source audit logs have been archived for compliance.</p>
            </div>
            <div className="bg-white/5 rounded-xl p-4 border border-white/10 space-y-2">
              <h3 className="text-xs font-bold uppercase tracking-wider text-chatgpt-secondary flex items-center gap-2">
                <AlertTriangle size={14} /> Risk Acknowledgement
              </h3>
              <p className="text-sm text-white">User acknowledged high-stakes risks and verified primary sources before finalization.</p>
            </div>
          </div>

          <div className="p-4 bg-evaluation-info/10 rounded-xl border border-evaluation-info/20 text-center">
            <p className="text-xs text-evaluation-info italic">
              "Trust but Verify: The human remains the Final Decision Maker (FDM)."
            </p>
          </div>
        </div>

        {/* Footer */}
        <div className="p-6 border-t border-white/10 bg-black/20 flex justify-center">
          <button 
            onClick={onBack}
            className="flex items-center gap-2 px-6 py-2 bg-white/5 hover:bg-white/10 rounded-lg text-sm font-medium transition-all"
          >
            <ArrowLeft size={16} /> Return to Chat
          </button>
        </div>
      </div>
    </div>
  )
}
