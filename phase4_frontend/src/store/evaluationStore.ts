import { create } from 'zustand';

export interface Claim {
  id: string;
  text: string;
  isVerified: boolean;
}

export interface EvaluationData {
  interaction_id: string;
  session_id: string;
  response: string;
  neutral_response: string;
  evaluation: {
    claims: string[];
    confidence: {
      score: number;
      reasoning: string;
    };
    bias: {
      bias_score: number;
      detected_patterns: string[];
      recommendation: string;
    };
    tone: {
      tone_breakdown: Record<string, number>;
      dominant_tone: string;
      clinical_index: number;
    };
    accountability: {
      reminder: string;
      human_review_required: boolean;
    };
    verification_steps: string[];
  };
}

interface Message {
  id: string;
  role: 'user' | 'assistant';
  content: string;
  neutralContent?: string;
  timestamp: number;
}

interface EvaluationState {
  isEvaluationMode: boolean;
  evaluationData: EvaluationData | null;
  verifiedClaims: string[];
  isLoading: boolean;
  sessionId: string | null;
  messages: Message[];
  
  setEvaluationMode: (mode: boolean) => void;
  setEvaluationData: (data: EvaluationData) => void;
  toggleClaimVerification: (claimId: string) => void;
  setLoading: (loading: boolean) => void;
  setSessionId: (id: string) => void;
  addMessage: (message: Message) => void;
  reset: () => void;
}

export const useEvaluationStore = create<EvaluationState>((set) => ({
  isEvaluationMode: true,
  evaluationData: null,
  verifiedClaims: [],
  isLoading: false,
  sessionId: null,
  messages: [],

  setEvaluationMode: (mode) => set({ isEvaluationMode: mode }),
  
  setEvaluationData: (data) => set((state) => ({
    evaluationData: data,
    verifiedClaims: [],
    isLoading: false,
    messages: [
      ...state.messages,
      {
        id: data.interaction_id,
        role: 'assistant',
        content: data.response,
        neutralContent: data.neutral_response,
        timestamp: Date.now()
      }
    ]
  })),

  toggleClaimVerification: (claimText) => set((state) => ({
    verifiedClaims: state.verifiedClaims.includes(claimText)
      ? state.verifiedClaims.filter(c => c !== claimText)
      : [...state.verifiedClaims, claimText]
  })),

  setLoading: (loading) => set({ isLoading: loading }),

  setSessionId: (id) => set({ sessionId: id }),

  addMessage: (message) => set((state) => ({
    messages: [...state.messages, message]
  })),

  reset: () => set({
    evaluationData: null,
    verifiedClaims: [],
    isLoading: false,
    messages: []
  })
}));
