# TaskBoard - Real-time Collaborative Task Management

A modern, full-stack task management application with real-time collaboration features. Built with React, TypeScript, Node.js, Express, and WebSocket.

![License](https://img.shields.io/badge/license-GPL--2.0-blue)
![Node](https://img.shields.io/badge/node-20%2B-brightgreen)
![React](https://img.shields.io/badge/react-19-blue)

## 🚀 Features

- **Real-time Collaboration**: Multiple users can work simultaneously with WebSocket updates
- **Kanban Board**: Organize tasks across Todo, In Progress, and Done columns
- **Modern UI**: Beautiful, responsive design with TailwindCSS
- **Type-Safe**: Full TypeScript implementation on both frontend and backend
- **RESTful API**: Well-structured REST API for task management
- **Docker Support**: Easy deployment with Docker Compose

## 📋 Prerequisites

- Node.js 20 or higher
- npm or yarn
- Docker and Docker Compose (optional, for containerized deployment)

## 🛠️ Tech Stack

### Frontend
- **React 19** - UI library
- **TypeScript** - Type safety
- **Vite** - Build tool and dev server
- **TailwindCSS** - Styling
- **WebSocket** - Real-time updates

### Backend
- **Node.js** - Runtime
- **Express** - Web framework
- **TypeScript** - Type safety
- **WebSocket (ws)** - Real-time communication
- **uuid** - Unique ID generation

### DevOps
- **Docker** - Containerization
- **Docker Compose** - Multi-container orchestration
- **Nginx** - Frontend serving and reverse proxy

## 🏃 Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/percy-raskova/copilots-playground.git
   cd copilots-playground
   ```

2. **Start the Backend**
   ```bash
   cd backend
   npm install
   npm run dev
   ```
   Backend will run on `http://localhost:3001`

3. **Start the Frontend** (in a new terminal)
   ```bash
   cd frontend
   npm install
   npm run dev
   ```
   Frontend will run on `http://localhost:5173`

4. **Open your browser**
   Navigate to `http://localhost:5173` and start managing tasks!

### Docker Deployment

Run the entire stack with Docker Compose:

```bash
docker-compose up --build
```

Access the application at `http://localhost`

## 📁 Project Structure

```
copilots-playground/
├── backend/                 # Backend API server
│   ├── src/
│   │   ├── models/         # Data models and types
│   │   ├── routes/         # API route handlers
│   │   ├── services/       # Business logic
│   │   ├── websocket.ts    # WebSocket setup
│   │   └── server.ts       # Main server file
│   ├── Dockerfile
│   ├── package.json
│   └── tsconfig.json
│
├── frontend/               # React frontend
│   ├── src/
│   │   ├── components/    # React components
│   │   ├── hooks/         # Custom React hooks
│   │   ├── services/      # API client
│   │   ├── types/         # TypeScript types
│   │   └── App.tsx        # Main App component
│   ├── Dockerfile
│   ├── nginx.conf
│   ├── package.json
│   └── tailwind.config.js
│
├── docker-compose.yml      # Docker orchestration
└── README.md              # This file
```

## 🎯 API Endpoints

### Tasks
- `GET /api/tasks` - Get all tasks
- `GET /api/tasks/:id` - Get task by ID
- `POST /api/tasks` - Create new task
- `PUT /api/tasks/:id` - Update task
- `DELETE /api/tasks/:id` - Delete task

### WebSocket
- `ws://localhost:3001/ws` - Real-time updates

## 🧪 Development Commands

### Backend
```bash
npm run dev      # Start development server with hot reload
npm run build    # Build for production
npm start        # Start production server
npm run lint     # Run ESLint
npm run format   # Format code with Prettier
```

### Frontend
```bash
npm run dev      # Start development server
npm run build    # Build for production
npm run preview  # Preview production build
```

## 🎨 Features in Detail

### Task Management
- Create tasks with title and description
- Move tasks between columns (Todo → In Progress → Done)
- Delete tasks
- Real-time updates across all connected clients

### Real-time Collaboration
- WebSocket connection for instant updates
- Connection status indicator
- Broadcast task changes to all users

### Responsive Design
- Mobile-friendly interface
- Smooth animations and transitions
- Modern color scheme

## 🔧 Configuration

### Backend Environment Variables
Create a `.env` file in the backend directory:
```env
PORT=3001
NODE_ENV=development
```

### Frontend API Configuration
Update `src/services/api.ts` if backend runs on a different URL.

## 🚢 Production Deployment

### Using Docker
```bash
docker-compose up -d
```

### Manual Deployment
1. Build backend: `cd backend && npm run build`
2. Build frontend: `cd frontend && npm run build`
3. Serve frontend `dist/` folder with Nginx
4. Run backend: `node dist/server.js`

## 🤝 Contributing

This is a playground repository - feel free to fork and experiment!

## 📝 License

This project is licensed under the GNU General Public License v2.0 - see the [LICENSE](LICENSE) file for details.

## 🎉 Acknowledgments

Created by AI Copilot as a demonstration of modern full-stack development practices.

---

**Built with ❤️ by AI** | Ready to use, customize, and deploy!
