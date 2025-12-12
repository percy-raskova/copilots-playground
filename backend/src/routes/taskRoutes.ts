import express, { Request, Response } from 'express';
import TaskService from '../services/TaskService';
import { CreateTaskDto, UpdateTaskDto } from '../models/Task';

const router = express.Router();

// Get all tasks
router.get('/', (req: Request, res: Response) => {
  const tasks = TaskService.getAllTasks();
  res.json(tasks);
});

// Get task by ID
router.get('/:id', (req: Request, res: Response) => {
  const task = TaskService.getTaskById(req.params.id);
  if (!task) {
    res.status(404).json({ error: 'Task not found' });
    return;
  }
  res.json(task);
});

// Create new task
router.post('/', (req: Request, res: Response) => {
  const dto: CreateTaskDto = req.body;
  if (!dto.title) {
    res.status(400).json({ error: 'Title is required' });
    return;
  }
  const task = TaskService.createTask(dto);
  res.status(201).json(task);
});

// Update task
router.put('/:id', (req: Request, res: Response) => {
  const dto: UpdateTaskDto = req.body;
  const task = TaskService.updateTask(req.params.id, dto);
  if (!task) {
    res.status(404).json({ error: 'Task not found' });
    return;
  }
  res.json(task);
});

// Delete task
router.delete('/:id', (req: Request, res: Response) => {
  const success = TaskService.deleteTask(req.params.id);
  if (!success) {
    res.status(404).json({ error: 'Task not found' });
    return;
  }
  res.status(204).send();
});

export default router;
