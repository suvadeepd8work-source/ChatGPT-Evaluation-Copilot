import { EvaluationData } from '../store/evaluationStore';

const API_BASE_URL = import.meta.env.VITE_API_URL || '/api/v1';

export const apiService = {
  async processEvaluation(prompt: string, sessionId?: string, userId?: string): Promise<EvaluationData> {
    const response = await fetch(`${API_BASE_URL}/evaluation/process`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        prompt,
        session_id: sessionId,
        user_id: userId,
      }),
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || 'Failed to process evaluation');
    }

    return response.json();
  },

  async logVerification(interactionId: string, type: string, details: any) {
    const response = await fetch(`${API_BASE_URL}/evaluation/verify/${interactionId}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        type,
        details,
      }),
    });

    if (!response.ok) {
      throw new Error('Failed to log verification');
    }

    return response.json();
  },

  async createSession(userId?: string) {
    const response = await fetch(`${API_BASE_URL}/sessions/create${userId ? `?user_id=${userId}` : ''}`, {
      method: 'POST',
    });

    if (!response.ok) {
      throw new Error('Failed to create session');
    }

    return response.json();
  }
};
