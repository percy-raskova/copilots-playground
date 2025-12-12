export interface Task {
  id: string;
  title: string;
  description: string;
  status: 'todo' | 'in-progress' | 'done';
  createdAt: Date;
  updatedAt: Date;
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
