export interface Task {
  id: string;
  title: string;
  description: string;
  status: 'todo' | 'in-progress' | 'done';
  createdAt: string;
  updatedAt: string;
}

export interface CreateTaskDto {
  title: string;
  description: string;
  status?: 'todo' | 'in-progress' | 'done';
}

export interface UpdateTaskDto {
  title?: string;
  description?: string;
  status?: 'todo' | 'in-progress' | 'done';
}
