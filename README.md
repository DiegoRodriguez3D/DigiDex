# DigiDex - Digital Gate

**[English](#english) | [Español](#español)**

---

## 🇬🇧 English

A modern, cyberpunk-themed Digimon encyclopedia built with SvelteKit and FastAPI.

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
| Deployment | VPS with Coolify |

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

### 📝 Environment Variables

| Service | Variable | Description |
|---------|----------|-------------|
| Backend | `FRONTEND_URL` | Vercel deployment URL for CORS |
| Frontend | `API_URL` | Render API URL with `/api/v1` path |

---

### 📄 License

MIT © 2024

---

*Data provided by [Digi-API](https://digi-api.com)*


## 🇪🇸 Español

Una enciclopedia Digimon moderna, con temática Cyberpunk, creada con SvelteKit y FastAPI

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
| Despliegue | VPS con Coolify |

### 📝 Variables de Entorno

| Servicio | Variable | Descripción |
|----------|----------|-------------|
| Backend | `FRONTEND_URL` | URL de Vercel para CORS |
| Frontend | `API_URL` | URL de Render API con path `/api/v1` |

---

### 📄 Licencia

MIT © 2024

---

*Datos proporcionados por [Digi-API](https://digi-api.com)*
