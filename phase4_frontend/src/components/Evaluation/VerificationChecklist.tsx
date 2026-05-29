import React from 'react'
import { ExternalLink, ClipboardCheck } from 'lucide-react'

interface Props {
  steps: string[]
}

export const VerificationChecklist = ({ steps }: Props) => {
  return (
    <div className="bg-evaluation-info/5 rounded-xl p-4 border border-evaluation-info/20">
      <h3 className="text-xs font-semibold uppercase tracking-wider text-evaluation-info flex items-center gap-1.5 mb-4">
        Verification Workflow <ClipboardCheck size={14} />
      </h3>
      
      <div className="space-y-4">
        {steps.map((step, index) => (
          <div key={index} className="flex items-start gap-3">
            <div className="w-5 h-5 rounded-full bg-evaluation-info/20 flex items-center justify-center text-[10px] text-evaluation-info shrink-0 mt-0.5">
              {index + 1}
            </div>
            <div className="flex-1">
              <p className="text-xs text-chatgpt-text/90 leading-relaxed mb-2">
                {step}
              </p>
              <button className="text-[10px] flex items-center gap-1 text-evaluation-info hover:underline">
                Source Audit <ExternalLink size={10} />
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
