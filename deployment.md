# Deployment Guide: ChatGPT Evaluation Mode

This document outlines the steps required to deploy the application in a production environment using **Vercel**.

## 1. Prerequisites
- A GitHub repository with the project code.
- A Vercel account.
- A [Groq API Key](https://console.groq.com/).

## 2. Vercel Configuration
The project is configured for Vercel using the [vercel.json](vercel.json) file in the root directory. This file handles:
- Routing for both the Frontend (React/Vite) and Backend (FastAPI).
- Python runtime configuration for the API.
- SPA routing to ensure `index.html` is served for all frontend routes.

## 3. Environment Variables
You must configure the following environment variables in the Vercel Dashboard (**Settings > Environment Variables**):

### **Backend Variables**
| Variable | Description | Example |
| :--- | :--- | :--- |
| `GROQ_API_KEY` | Your Groq API Key | `gsk_...` |
| `DATABASE_URL` | SQLite path or PostgreSQL URL | `sqlite:///./storage/prod.db` |
| `ENVIRONMENT` | Deployment environment | `production` |
| `FRONTEND_URL` | The production URL of your frontend | `https://your-app.vercel.app` |

### **Frontend Variables**
| Variable | Description | Example |
| :--- | :--- | :--- |
| `VITE_API_URL` | The base URL for API calls | `/api/v1` (Default) |

## 4. Deployment Steps
1. **Import Project**: In Vercel, click "New Project" and import your GitHub repository.
2. **Configure Root**: Ensure the "Root Directory" is set to the repository root.
3. **Build Settings**: 
   - Build Command: `npm run build` (inside `phase4_frontend`)
   - Output Directory: `phase4_frontend/dist`
4. **Environment Variables**: Add the variables listed in section 3.
5. **Deploy**: Click "Deploy".

## 5. Performance & Monitoring
- **Error Logging**: The backend uses Python's standard `logging` module. In Vercel, these logs are accessible via the **Functions** tab.
- **Frontend Performance**: Vite handles production minification and code splitting automatically.
- **API Optimization**: The `vercel.json` configuration uses serverless functions for the FastAPI backend, ensuring scalability.

## 6. Security
- **CORS**: Production CORS is restricted to the `FRONTEND_URL` in [main.py](phase3_backend/main.py).
- **API Docs**: Swagger UI (`/api/docs`) is disabled in production to prevent exposure of API schemas.
- **Environment Handling**: Never commit `.env` files. Always use the Vercel Dashboard for secret management.
