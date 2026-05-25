# TerraInsights

TerraInsights is a full-stack project with:

- `frontend/`: React + Vite web app
- `backend/`: FastAPI API with a scikit-learn model
- `ml/`: trained fertilizer recommendation model

## Local run

Backend:

```powershell
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Frontend:

```powershell
cd frontend
npm install
$env:VITE_API_BASE_URL="http://localhost:8000"
npm run dev
```

## Deploy

The simplest production setup for this repo is:

- `frontend/` on Vercel
- `backend/` on Render

### 1. Deploy the backend on Render

Create a new **Web Service** from the `backend` folder.

- Build command: `pip install -r requirements.txt`
- Start command: `uvicorn main:app --host 0.0.0.0 --port 10000`

Environment variables:

- `FRONTEND_ORIGIN=https://your-frontend-domain.vercel.app`
- Optional: `DATABASE_URL=sqlite:///./sqlite.db`

Notes:

- The current project uses SQLite. That is fine for demos, but hosted SQLite is usually not durable on free cloud instances.
- If you want prediction history to persist reliably, move `DATABASE_URL` to a managed Postgres database later.
- After deploy, confirm `https://your-backend-domain.onrender.com/health` returns `{"status":"ok","model_loaded":true}`.

### 2. Deploy the frontend on Vercel

Create a new Vercel project using the `frontend` folder.

Settings:

- Framework preset: `Vite`
- Build command: `npm run build`
- Output directory: `dist`

Environment variables:

- `VITE_API_BASE_URL=https://your-backend-domain.onrender.com`

### 3. Update backend CORS

Once the Vercel URL is final, set:

```text
FRONTEND_ORIGIN=https://your-frontend-domain.vercel.app
```

If you later add a custom domain, include that domain instead.

## Production caveats

- The frontend was previously hardcoded to `localhost`; it now uses `VITE_API_BASE_URL`.
- Prediction history is stored in the backend database. On SQLite, that may reset depending on your host.
- The ML model file at `ml/fertilizer_model.pkl` must be present in the deployed repo.
