# Goal Description

Build a "Sustainable Fertilizer Usage Optimizer for Higher Yield" full-stack web application. The application will analyze soil and crop data using a Machine Learning model to recommend optimal fertilizers, promoting sustainable farming and higher yields.

## User Review Required

> [!IMPORTANT]
> Please review the proposed technology stack and design approach:
> - **Frontend**: React via Vite. As per guidelines, I will use **Vanilla CSS** with rich modern aesthetics (gradients, glassmorphism, micro-animations) instead of TailwindCSS.
> - **Backend**: Python with FastAPI. It's lightweight and integrates seamlessly with Python ML libraries.
> - **Machine Learning**: Scikit-learn (Random Forest or XGBoost) to train a classification model on `fertilizer_recommendation.csv` to predict the `Recommended_Fertilizer`.
> - **User Database**: SQLite, as requested.

## Proposed Changes

---

### Machine Learning Model
We will create a script to train and save the model based on the provided dataset.
#### [NEW] `ml/train_model.py` - Script to preprocess data, train a classification model, and save it.
#### [NEW] `ml/fertilizer_model.pkl` - The trained model artifact.
#### [NEW] `ml/label_encoders.pkl` - Saved encoders for categorical variables (Soil Type, Crop Type, etc.)

---

### Backend (Python FastAPI)
A REST API to handle user authentication, serve ML predictions, and manage user data.
#### [NEW] `backend/requirements.txt` - Dependencies (`fastapi`, `uvicorn`, `scikit-learn`, `pandas`, `sqlalchemy`).
#### [NEW] `backend/main.py` - Main FastAPI application and API routes (auth, prediction, user profile).
#### [NEW] `backend/database.py` - SQLAlchemy configuration for SQLite.
#### [NEW] `backend/models.py` - Database schemas (User table, History table).

---

### Frontend (React + Vite)
We will build a responsive, highly animated, and premium UI.
#### [NEW] `frontend/package.json` - React dependencies.
#### [NEW] `frontend/index.html` - App entry point with modern web fonts (e.g., Inter).
#### [NEW] `frontend/src/index.css` - Global Vanilla CSS implementing the design system (variables, animations, utility classes).
#### [NEW] `frontend/src/App.jsx` - Main router handling all the pages.
#### [NEW] `frontend/src/pages/LandingPage.jsx` - Landing page with navbar.
#### [NEW] `frontend/src/pages/AuthPage.jsx` - Sign-in / Sign-up page.
#### [NEW] `frontend/src/pages/DashboardPage.jsx` - ML model integration and results.
#### [NEW] `frontend/src/pages/ProfilePage.jsx` - User profile.
#### [NEW] `frontend/src/pages/AboutPage.jsx` - About the project.
#### [NEW] `frontend/src/pages/StorePage.jsx` - Fertilizer store based on recommendations.
#### [NEW] `frontend/src/pages/AgroGuidePage.jsx` - Educational content with filters.
#### [NEW] `frontend/src/pages/GovtSchemesPage.jsx` - Farmer perks and benefits.

## Open Questions

> [!WARNING]
> I need your input on a few items before proceeding:
> 1. **Store functionality**: Should the Store/Shop page have real payment integration, or just a front-end UI demonstration?
> 2. **Mock data**: For pages like Agroguide and Govt Schemes, should I generate realistic mock data using AI, or do you have a specific list of schemes/guides you want to include?
> 3. Does the proposed technology stack (React + FastAPI + SQLite + Scikit-Learn) sound good to you?

## Verification Plan

### Automated Tests
- Train the model and evaluate accuracy (F1-score/Accuracy).
- Start the FastAPI backend and test API endpoints.
- Build the Vite frontend to ensure no compilation errors.

### Manual Verification
- View the UI through the browser tool to confirm aesthetics are "premium", dynamic, and responsive.
- Test the complete flow: User Sign Up -> Login -> Dashboard -> Enter Soil Parameters -> Get Fertilizer Recommendation -> View in Store.
