# Contributing to TaskBoard

Thank you for your interest in contributing to TaskBoard! This is a playground repository, so feel free to experiment and try new things.

## Development Setup

1. **Prerequisites**
   - Node.js 20 or higher
   - npm or yarn
   - Git

2. **Clone and Install**
   ```bash
   git clone https://github.com/percy-raskova/copilots-playground.git
   cd copilots-playground
   
   # Install backend dependencies
   cd backend
   npm install
   
   # Install frontend dependencies
   cd ../frontend
   npm install
   ```

3. **Running Locally**
   ```bash
   # Terminal 1: Backend
   cd backend
   npm run dev
   
   # Terminal 2: Frontend
   cd frontend
   npm run dev
   ```

## Project Structure

```
├── backend/          # Express API server
│   ├── src/
│   │   ├── models/   # Data models
│   │   ├── routes/   # API routes
│   │   ├── services/ # Business logic
│   │   └── server.ts # Entry point
│   └── Dockerfile
│
├── frontend/         # React application
│   ├── src/
│   │   ├── components/ # UI components
│   │   ├── hooks/      # Custom hooks
│   │   ├── services/   # API client
│   │   └── types/      # TypeScript types
│   └── Dockerfile
│
└── docker-compose.yml
```

## Coding Standards

### Backend
- Use TypeScript
- Follow the existing code structure
- Use async/await for asynchronous operations
- Add JSDoc comments for complex functions

### Frontend
- Use TypeScript
- Use functional components with hooks
- Follow React best practices
- Use TailwindCSS for styling

## Code Formatting

```bash
# Backend
cd backend
npm run format
npm run lint

# Frontend
cd frontend
npm run format (if added)
```

## Testing

Currently, basic manual testing is in place. Contributions to add automated tests are welcome!

## Pull Request Process

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test your changes
5. Submit a pull request

## Ideas for Contributions

- Add unit tests
- Add drag-and-drop functionality
- Add user authentication
- Add task categories/tags
- Add task priority levels
- Add due dates
- Improve mobile responsiveness
- Add dark mode
- Add data persistence (database)
- Add task search/filter

## Questions?

This is a learning and experimentation repository. Don't hesitate to try new things!

## License

This project is licensed under GPL-2.0 - see the [LICENSE](LICENSE) file for details.
