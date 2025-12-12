import React from 'react';
import { Task } from '../types/Task';
import { TaskCard } from './TaskCard';

interface TaskColumnProps {
  title: string;
  status: Task['status'];
  tasks: Task[];
  onDelete: (id: string) => void;
  onStatusChange: (id: string, status: Task['status']) => void;
}

export const TaskColumn: React.FC<TaskColumnProps> = ({
  title,
  status,
  tasks,
  onDelete,
  onStatusChange,
}) => {
  const columnColors = {
    todo: 'bg-gray-50',
    'in-progress': 'bg-blue-50',
    done: 'bg-green-50',
  };

  const filteredTasks = tasks.filter((task) => task.status === status);

  return (
    <div className={`flex-1 ${columnColors[status]} rounded-lg p-4 min-w-[300px]`}>
      <div className="flex justify-between items-center mb-4">
        <h2 className="text-xl font-bold text-gray-700">{title}</h2>
        <span className="bg-white rounded-full px-3 py-1 text-sm font-semibold text-gray-600">
          {filteredTasks.length}
        </span>
      </div>
      <div className="space-y-3">
        {filteredTasks.map((task) => (
          <TaskCard
            key={task.id}
            task={task}
            onDelete={onDelete}
            onStatusChange={onStatusChange}
          />
        ))}
        {filteredTasks.length === 0 && (
          <div className="text-center text-gray-400 py-8">No tasks</div>
        )}
      </div>
    </div>
  );
};
