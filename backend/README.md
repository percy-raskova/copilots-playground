# TaskBoard Backend

RESTful API server with WebSocket support for real-time task management.

## Features

- Express.js REST API
- WebSocket for real-time updates
- TypeScript for type safety
- In-memory task storage
- CORS enabled for frontend communication

## API Documentation

### Get All Tasks
```http
GET /api/tasks
```

### Get Task by ID
```http
GET /api/tasks/:id
```

### Create Task
```http
POST /api/tasks
Content-Type: application/json

{
  "title": "Task title",
  "description": "Task description",
  "status": "todo"  // optional: "todo" | "in-progress" | "done"
}
```

### Update Task
```http
PUT /api/tasks/:id
Content-Type: application/json

{
  "title": "Updated title",
  "description": "Updated description",
  "status": "in-progress"
}
```

### Delete Task
```http
DELETE /api/tasks/:id
```

## WebSocket Events

Connect to `ws://localhost:3001/ws`

### Message Format
```json
{
  "type": "task-update",
  "action": "create" | "update" | "delete",
  "taskId": "uuid"
}
```

## Development

```bash
# Install dependencies
npm install

# Run development server with hot reload
npm run dev

# Build for production
npm run build

# Start production server
npm start
```

## Environment Variables

- `PORT` - Server port (default: 3001)
- `NODE_ENV` - Environment (development/production)
