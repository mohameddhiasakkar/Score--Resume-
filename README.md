# 📄 Score Resume

An intelligent **Resume Analysis Platform** built with **Angular + Django REST Framework**.

Score Resume helps users upload their CVs, analyze resume quality, and receive useful feedback to improve their chances in the job market.

---

## 🚀 Features

- 📤 Upload resumes (PDF)
- 📊 Resume scoring system
- 🤖 AI-powered resume analysis
- 🔍 Extract resume information
- 📝 Improvement suggestions
- 🌐 REST API backend
- 🐳 Dockerized application
- ☁️ Deployment ready with Render

---

## 🏗️ Architecture

```text
Score--Resume-
│
├── frontend/              # Angular frontend
│
├── mybackend/             # Django REST API
│   ├── core_api/
│   ├── ai_engine/
│   ├── cvapp/
│   └── config/
│
└── docker-compose.yml
