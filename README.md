# CyberShield AI - Email Spam Detection System

A complete full-stack email spam detection web application with a futuristic cybersecurity dashboard UI.

## Project Structure

```bash
ai_spam_cyber/
├── backend/
│   ├── app.py
│   ├── train_model.py
│   ├── spam.csv
│   ├── requirements.txt
│   ├── Procfile
│   ├── runtime.txt
│   └── .env.example
├── frontend/
│   ├── public/
│   │   ├── favicon.svg
│   │   └── logo.svg
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── App.jsx
│   │   ├── index.css
│   │   └── main.jsx
│   ├── package.json
│   ├── postcss.config.js
│   ├── tailwind.config.js
│   ├── vite.config.js
│   └── .env.example
└── README.md
```

## Local Development

### 1) Backend

```bash
cd backend
pip install -r requirements.txt
python train_model.py
python app.py
```

Backend runs on `http://127.0.0.1:5000`.

### 2) Frontend

```bash
cd frontend
cp .env.example .env
npm install
npm run dev
```

Frontend runs on `http://127.0.0.1:5173`.

## Environment Variables

### Frontend

```env
VITE_API_BASE_URL=http://127.0.0.1:5000
```

### Backend

```env
PORT=5000
```

## Vercel Deployment

- Framework preset: `Vite`
- Root directory: `frontend`
- Build command: `npm run build`
- Output directory: `dist`
- Environment variable: `VITE_API_BASE_URL=https://YOUR-RENDER-URL.onrender.com`

## Render Deployment

- Root directory: `backend`
- Build command: `pip install -r requirements.txt && python train_model.py`
- Start command: `gunicorn app:app`
- Environment variable: `PORT=10000` (Render usually injects this automatically)

## API Contract

### `POST /predict`

Request:

```json
{
  "email": "Urgent: verify your account now"
}
```

Response:

```json
{
  "prediction": "spam",
  "confidence": 0.95,
  "scores": {
    "spam": 0.95,
    "ham": 0.05
  },
  "insights": {
    "messageLength": 36,
    "suspiciousTerms": ["urgent", "verify", "account"],
    "riskLevel": "critical"
  }
}
```

## Notes

- The included dataset is a compact demo dataset for development.
- Replace `spam.csv` with a larger dataset to improve production accuracy.
- The contact form is UI-ready and can be wired to Formspree, Resend, or a custom backend.
