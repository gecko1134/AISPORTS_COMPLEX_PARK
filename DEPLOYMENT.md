# Deployment Guide

## 🧱 Requirements

- PostgreSQL host (e.g., Supabase, Neon, Render)
- Python 3.10+
- Streamlit

## 🛠 Cloud Deployment Options

### 1. Render (Recommended for Streamlit + PostgreSQL)
- Create new PostgreSQL instance
- Create new Web Service with:
  - Build Command: `pip install -r requirements.txt`
  - Start Command: `streamlit run dashboard.py`

### 2. Railway.app
- Deploy via GitHub repo
- Add `DATABASE_URL` as an environment variable
- Configure to run `streamlit run admin.py`

### 3. Supabase (PostgreSQL only)
- Provision a DB
- Copy connection string as `DATABASE_URL`
- Use for local or cloud Streamlit app

## ✅ GitHub Actions CI

Create a repository secret:
- `DATABASE_URL` = your PostgreSQL URL

This runs a DB connectivity test on each push to `main`.

---
