# Deployment Guide: ChatGPT Evaluation Mode

This document outlines the steps required to deploy the application in a production environment using **Vercel** (Frontend) and **Render** (Backend).

## 1. Prerequisites
- A GitHub repository with the project code.
- A [Vercel](https://vercel.com/) account for the frontend.
- A [Render](https://render.com/) account for the backend.
- A [Groq API Key](https://console.groq.com/).

---

## 2. Backend Deployment (Render)

### **Step 1: Create a Blueprint Instance**
1. Log in to Render.
2. Click **New > Blueprint**.
3. Connect your GitHub repository.
4. Render will detect the `render.yaml` file and prepare the service.

### **Step 2: Environment Variables**
Configure the following in the Render Dashboard (or via the Blueprint prompt):
- `GROQ_API_KEY`: Your production API key.
- `FRONTEND_URL`: Your Vercel frontend URL (e.g., `https://chat-gpt-evaluation-copilot.vercel.app`).
- `ENVIRONMENT`: `production`.

### **Step 3: Persistence**
The `render.yaml` includes a **Disk** definition to ensure your SQLite database (`evaluation.db`) persists across restarts.

---

## 3. Frontend Deployment (Vercel)

### **Step 1: Configure Vercel**
1. Import your GitHub repository into Vercel.
2. **Root Directory**: Select `phase4_frontend`.
3. **Framework Preset**: Vite.
4. **Build Command**: `npm run build`.
5. **Output Directory**: `dist`.

### **Step 2: Environment Variables**
Add the following in **Settings > Environment Variables**:
- `VITE_API_URL`: Your Render backend URL (e.g., `https://chatgpt-evaluation-backend.onrender.com/api/v1`).

---

## 4. Scheduler (GitHub Actions)
The scheduler is configured in `.github/workflows/scheduler.yml`. It runs daily at 10 AM UTC.
- **Secret Required**: Add `DATABASE_URL` or `BACKEND_URL` to your GitHub Repository Secrets if the scheduler needs to trigger remote updates.

---

## 5. Verification Steps
1. **Backend Health**: Visit `https://your-backend.onrender.com/health`.
2. **CORS Check**: Ensure the frontend can successfully call the backend without console errors.
3. **Persistence**: Create a session in the app, restart the Render service, and verify the session still exists.
