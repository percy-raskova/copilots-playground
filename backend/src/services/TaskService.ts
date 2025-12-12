import { v4 as uuidv4 } from 'uuid';
import { Task, CreateTaskDto, UpdateTaskDto } from '../models/Task';

class TaskService {
  private tasks: Map<string, Task> = new Map();

  constructor() {
    // Initialize with some sample tasks
    this.createTask({
      title: 'Welcome to TaskBoard!',
      description: 'This is a sample task. Try moving it between columns!',
      status: 'todo',
    });
    this.createTask({
      title: 'Set up development environment',
      description: 'Install dependencies and configure the project',
      status: 'in-progress',
    });
    this.createTask({
      title: 'Deploy to production',
      description: 'Configure CI/CD and deploy the application',
      status: 'todo',
    });
  }

  getAllTasks(): Task[] {
    return Array.from(this.tasks.values());
  }

  getTaskById(id: string): Task | undefined {
    return this.tasks.get(id);
  }

  createTask(dto: CreateTaskDto): Task {
    const task: Task = {
      id: uuidv4(),
      title: dto.title,
      description: dto.description,
      status: dto.status || 'todo',
      createdAt: new Date(),
      updatedAt: new Date(),
    };
    this.tasks.set(task.id, task);
    return task;
  }

  updateTask(id: string, dto: UpdateTaskDto): Task | null {
    const task = this.tasks.get(id);
    if (!task) {
      return null;
    }

    const updatedTask: Task = {
      ...task,
      ...dto,
      updatedAt: new Date(),
    };
    this.tasks.set(id, updatedTask);
    return updatedTask;
  }

  deleteTask(id: string): boolean {
    return this.tasks.delete(id);
  }
}

export default new TaskService();
