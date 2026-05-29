import React from 'react'
import { ShieldAlert, UserCheck } from 'lucide-react'

interface Props {
  reminder: string
  required: boolean
}

export const AccountabilityReminder = ({ reminder, required }: Props) => {
  return (
    <div className={`rounded-xl p-4 border ${
      required 
        ? 'bg-evaluation-error/10 border-evaluation-error/30 animate-pulse' 
        : 'bg-white/5 border-white/10'
    }`}>
      <div className="flex items-start gap-3">
        <div className={required ? 'text-evaluation-error' : 'text-chatgpt-secondary'}>
          {required ? <ShieldAlert size={20} /> : <UserCheck size={20} />}
        </div>
        <div>
          <h3 className={`text-xs font-bold uppercase tracking-wider mb-1 ${
            required ? 'text-evaluation-error' : 'text-chatgpt-secondary'
          }`}>
            Human Accountability Reminder
          </h3>
          <p className="text-sm text-chatgpt-text font-medium leading-snug">
            {reminder}
          </p>
          {required && (
            <p className="text-[10px] text-evaluation-error mt-2 font-bold uppercase">
              MANDATORY SIGN-OFF REQUIRED
            </p>
          )}
        </div>
      </div>
    </div>
  )
}
