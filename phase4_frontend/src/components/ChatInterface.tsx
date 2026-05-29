import React, { useState, useEffect } from 'react'
import { Send, Shield, User, Bot, Loader2 } from 'lucide-react'
import { useEvaluationStore } from '../store/evaluationStore'
import { apiService } from '../services/api'
import { clsx } from 'clsx'
import { MessageRenderer } from './MessageRenderer'

export const ChatInterface = () => {
  const [input, setInput] = useState('')
  const { 
    isEvaluationMode, 
    setEvaluationMode, 
    isLoading, 
    setLoading, 
    setEvaluationData, 
    sessionId, 
    setSessionId,
    messages,
    addMessage
  } = useEvaluationStore()

  // Initialize session on mount
  useEffect(() => {
    if (!sessionId) {
      apiService.createSession().then(data => {
        setSessionId(data.session_id)
      })
    }
  }, [sessionId, setSessionId])

  const handleSend = async () => {
    if (!input.trim() || isLoading) return
    
    const userMessage = {
      id: Math.random().toString(36).substring(7),
      role: 'user' as const,
      content: input,
      timestamp: Date.now()
    }
    
    addMessage(userMessage)
    setInput('')
    setLoading(true)

    try {
      if (isEvaluationMode) {
        const data = await apiService.processEvaluation(input, sessionId || undefined)
        setEvaluationData(data)
      } else {
        // Fallback for non-evaluation mode (simple echo for now or direct LLM)
        // In a real app, you'd have a separate endpoint for standard chat
        setTimeout(() => {
          addMessage({
            id: Math.random().toString(36).substring(7),
            role: 'assistant',
            content: `Standard Mode: You asked "${input}". Switch to Evaluation Mode for detailed analysis.`,
            timestamp: Date.now()
          })
          setLoading(false)
        }, 1000)
      }
    } catch (error) {
      console.error('Failed to send message:', error)
      setLoading(false)
    }
  }

  return (
    <div className="flex-1 flex flex-col h-full max-w-4xl mx-auto w-full border-r border-white/10 relative">
      {/* Header */}
      <div className="p-4 border-b border-white/10 flex items-center justify-between bg-chatgpt-gray/80 backdrop-blur-sm sticky top-0 z-10">
        <h1 className="text-lg font-semibold flex items-center gap-2">
          ChatGPT <span className="text-chatgpt-secondary font-normal">Evaluation Mode</span>
        </h1>
        
        {/* Evaluation Toggle */}
        <div className="flex items-center gap-3 bg-white/5 p-1 rounded-lg">
          <button 
            onClick={() => setEvaluationMode(false)}
            className={clsx(
              "px-3 py-1.5 text-xs rounded-md transition-all",
              !isEvaluationMode ? "bg-white/10 text-white shadow-sm" : "text-chatgpt-secondary hover:text-white"
            )}
          >
            Standard
          </button>
          <button 
            onClick={() => setEvaluationMode(true)}
            className={clsx(
              "px-3 py-1.5 text-xs rounded-md transition-all flex items-center gap-1.5",
              isEvaluationMode ? "bg-evaluation-primary text-white shadow-sm" : "text-chatgpt-secondary hover:text-white"
            )}
          >
            <Shield size={14} /> Evaluation
          </button>
        </div>
      </div>

      {/* Message List */}
      <div className="flex-1 overflow-y-auto p-4 space-y-6">
        {messages.length === 0 ? (
          <div className="max-w-2xl mx-auto mt-20 text-center">
            <div className="mb-4 inline-flex p-3 rounded-full bg-evaluation-primary/10 text-evaluation-primary">
              <Shield size={32} />
            </div>
            <h2 className="text-2xl font-bold mb-2">Welcome to Evaluation Mode</h2>
            <p className="text-chatgpt-secondary text-sm">
              This mode prioritizes factual verification and identifies AI bias.
              Try asking a high-stakes question to see the system in action.
            </p>
          </div>
        ) : (
          <div className="max-w-3xl mx-auto space-y-8 py-8">
            {messages.map((msg) => (
              <div key={msg.id} className="flex gap-4">
                <div className={clsx(
                  "w-8 h-8 rounded flex items-center justify-center shrink-0",
                  msg.role === 'user' ? "bg-white/10" : "bg-evaluation-primary"
                )}>
                  {msg.role === 'user' ? <User size={18} /> : <Bot size={18} />}
                </div>
                <div className="flex-1 space-y-2">
                  <p className="text-sm font-semibold">
                    {msg.role === 'user' ? 'You' : 'Assistant'}
                  </p>
                  <MessageRenderer 
                    original={msg.content} 
                    neutral={msg.neutralContent || msg.content} 
                    isEvaluationMode={isEvaluationMode && msg.role === 'assistant'} 
                  />
                </div>
              </div>
            ))}
            {isLoading && (
              <div className="flex gap-4 animate-pulse">
                <div className="w-8 h-8 rounded bg-evaluation-primary flex items-center justify-center shrink-0">
                  <Loader2 size={18} className="animate-spin" />
                </div>
                <div className="flex-1 space-y-2">
                  <p className="text-sm font-semibold text-chatgpt-secondary">Assistant is thinking...</p>
                  <div className="h-4 bg-white/5 rounded w-3/4"></div>
                  <div className="h-4 bg-white/5 rounded w-1/2"></div>
                </div>
              </div>
            )}
          </div>
        )}
      </div>

      {/* Input Area */}
      <div className="p-4 bg-gradient-to-t from-chatgpt-gray via-chatgpt-gray to-transparent">
        <div className="max-w-3xl mx-auto relative group">
          <textarea
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault()
                handleSend()
              }
            }}
            placeholder="Ask anything (e.g., 'Should I invest in Bitcoin?')"
            className="w-full bg-white/5 border border-white/10 rounded-xl px-4 py-4 pr-12 focus:outline-none focus:ring-1 focus:ring-evaluation-primary transition-all resize-none min-h-[60px]"
            rows={2}
          />
          <button 
            onClick={handleSend}
            disabled={!input.trim() || isLoading}
            className="absolute right-3 bottom-3 p-2 bg-white text-black rounded-lg hover:bg-gray-200 disabled:opacity-50 disabled:cursor-not-allowed transition-all"
          >
            {isLoading ? <Loader2 size={18} className="animate-spin" /> : <Send size={18} />}
          </button>
        </div>
        <p className="text-[10px] text-center mt-2 text-chatgpt-secondary">
          Evaluation Mode provides an additional layer of critical analysis for high-stakes decisions.
        </p>
      </div>
    </div>
  )
}
