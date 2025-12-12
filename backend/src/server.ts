import express from 'express';
import cors from 'cors';
import http from 'http';
import taskRoutes from './routes/taskRoutes';
import { setupWebSocket } from './websocket';

const app = express();
const PORT = process.env.PORT || 3001;

// Middleware
app.use(cors());
app.use(express.json());

// Routes
app.get('/', (req, res) => {
  res.json({
    message: 'TaskBoard API',
    version: '1.0.0',
    endpoints: {
      tasks: '/api/tasks',
      websocket: 'ws://localhost:3001/ws',
    },
  });
});

app.use('/api/tasks', taskRoutes);

// Create HTTP server
const server = http.createServer(app);

// Setup WebSocket
setupWebSocket(server);

// Start server
server.listen(PORT, () => {
  console.log(`🚀 Server running on http://localhost:${PORT}`);
  console.log(`📡 WebSocket available on ws://localhost:${PORT}/ws`);
});
