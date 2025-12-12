import React from 'react';
import { Task } from '../types/Task';

interface TaskCardProps {
  task: Task;
  onDelete: (id: string) => void;
  onStatusChange: (id: string, status: Task['status']) => void;
}

export const TaskCard: React.FC<TaskCardProps> = ({ task, onDelete, onStatusChange }) => {
  const statusColors = {
    todo: 'bg-gray-100 border-gray-300',
    'in-progress': 'bg-blue-50 border-blue-300',
    done: 'bg-green-50 border-green-300',
  };

  const getNextStatus = (currentStatus: Task['status']): Task['status'] => {
    const cycle: Task['status'][] = ['todo', 'in-progress', 'done'];
    const currentIndex = cycle.indexOf(currentStatus);
    return cycle[(currentIndex + 1) % cycle.length];
  };

  return (
    <div className={`border-2 rounded-lg p-4 mb-3 ${statusColors[task.status]} transition-all hover:shadow-md`}>
      <div className="flex justify-between items-start mb-2">
        <h3 className="font-semibold text-lg text-gray-800">{task.title}</h3>
        <button
          onClick={() => onDelete(task.id)}
          className="text-red-500 hover:text-red-700 text-xl font-bold"
          aria-label="Delete task"
        >
          ×
        </button>
      </div>
      <p className="text-gray-600 text-sm mb-3">{task.description}</p>
      <div className="flex justify-between items-center">
        <span className="text-xs text-gray-500">
          {new Date(task.updatedAt).toLocaleDateString()}
        </span>
        <button
          onClick={() => onStatusChange(task.id, getNextStatus(task.status))}
          className="px-3 py-1 text-sm bg-white rounded border border-gray-300 hover:bg-gray-50"
        >
          Move →
        </button>
      </div>
    </div>
  );
};
