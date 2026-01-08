# 🦖 DigiDex - Digital Gate

A modern, cyberpunk-themed Digimon encyclopedia built with SvelteKit and FastAPI.

**[English](#english) | [Español](#español)**

---

## English

### 🎮 Features

- **Grid View**: Browse 1400+ Digimon with paginated grid display
- **Detail View**: Comprehensive Digimon profiles with stats, skills, evolutions
- **Search**: Find Digimon by name instantly
- **Theme Toggle**: Switch between light and dark cyberpunk themes
- **Responsive**: Mobile-first design that works on all devices

### 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | SvelteKit, Tailwind CSS v4, TypeScript |
| Backend | FastAPI, Python 3.11+, httpx |
| Data Source | [Digi-API](https://digi-api.com) |
| Deployment | Vercel (Frontend), Render (Backend) |

### 📁 Project Structure

```
DigiDex/
├── backend/               # FastAPI BFF server
│   ├── api/v1/           # API endpoints
│   ├── schemas/          # Pydantic models
│   ├── services/         # External API client
│   ├── main.py           # App entry point
│   └── requirements.txt  # Python dependencies
├── frontend/             # SvelteKit app
│   ├── src/
│   │   ├── lib/components/  # Svelte components
│   │   ├── routes/          # Pages and server loaders
│   │   └── app.css          # Global styles
│   └── package.json
└── render.yaml           # Render deployment config
```

### 🚀 Local Development

#### Prerequisites
- Python 3.11+
- Node.js 20+
- npm or pnpm

#### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

#### Frontend
```bash
cd frontend
npm install
npm run dev
```

Open http://localhost:5173

### 🌐 Deployment

#### Backend (Render)
1. Create a new Web Service on [render.com](https://render.com)
2. Connect your repository
3. Configure:
   - **Root Directory**: `backend`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
4. Add environment variable: `FRONTEND_URL=https://your-app.vercel.app`

#### Frontend (Vercel)
1. Import project on [vercel.com](https://vercel.com)
2. Configure:
   - **Root Directory**: `frontend`
   - **Framework**: SvelteKit (auto-detected)
3. Add environment variable: `API_URL=https://your-api.onrender.com/api/v1`

### 📝 Environment Variables

| Service | Variable | Description |
|---------|----------|-------------|
| Backend | `FRONTEND_URL` | Vercel deployment URL for CORS |
| Frontend | `API_URL` | Render API URL with `/api/v1` path |

---

## Español

### 🎮 Características

- **Vista de Grid**: Explora más de 1400 Digimon con paginación
- **Vista de Detalle**: Perfiles completos con estadísticas, habilidades y evoluciones
- **Búsqueda**: Encuentra Digimon por nombre instantáneamente
- **Cambio de Tema**: Alterna entre temas claro y oscuro cyberpunk
- **Responsive**: Diseño mobile-first que funciona en todos los dispositivos

### 🛠️ Stack Tecnológico

| Capa | Tecnología |
|------|------------|
| Frontend | SvelteKit, Tailwind CSS v4, TypeScript |
| Backend | FastAPI, Python 3.11+, httpx |
| Fuente de Datos | [Digi-API](https://digi-api.com) |
| Despliegue | Vercel (Frontend), Render (Backend) |

### 🚀 Desarrollo Local

#### Requisitos
- Python 3.11+
- Node.js 20+
- npm o pnpm

#### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

#### Frontend
```bash
cd frontend
npm install
npm run dev
```

Abre http://localhost:5173

### 🌐 Despliegue

#### Backend (Render)
1. Crea un nuevo Web Service en [render.com](https://render.com)
2. Conecta tu repositorio
3. Configura:
   - **Root Directory**: `backend`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
4. Añade variable de entorno: `FRONTEND_URL=https://tu-app.vercel.app`

#### Frontend (Vercel)
1. Importa el proyecto en [vercel.com](https://vercel.com)
2. Configura:
   - **Root Directory**: `frontend`
   - **Framework**: SvelteKit (auto-detectado)
3. Añade variable de entorno: `API_URL=https://tu-api.onrender.com/api/v1`

### 📝 Variables de Entorno

| Servicio | Variable | Descripción |
|----------|----------|-------------|
| Backend | `FRONTEND_URL` | URL de Vercel para CORS |
| Frontend | `API_URL` | URL de Render API con path `/api/v1` |

---

## 📄 License

MIT © 2024

---

*Data provided by [Digi-API](https://digi-api.com)*
