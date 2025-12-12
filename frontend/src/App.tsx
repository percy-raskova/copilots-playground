import React, { useState, useEffect } from 'react';
import { Task, CreateTaskDto } from './types/Task';
import { taskApi } from './services/api';
import { useWebSocket } from './hooks/useWebSocket';
import { TaskColumn } from './components/TaskColumn';
import { AddTaskModal } from './components/AddTaskModal';

function App() {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const { isConnected, lastMessage, sendMessage } = useWebSocket('ws://localhost:3001/ws');

  useEffect(() => {
    loadTasks();
  }, []);

  useEffect(() => {
    if (lastMessage && lastMessage.type === 'task-update') {
      loadTasks();
    }
  }, [lastMessage]);

  const loadTasks = async () => {
    try {
      const data = await taskApi.getAllTasks();
      setTasks(data);
      setError(null);
    } catch (err) {
      setError('Failed to load tasks. Make sure the backend is running.');
      console.error(err);
    }
  };

  const handleAddTask = async (dto: CreateTaskDto) => {
    try {
      const newTask = await taskApi.createTask(dto);
      setTasks([...tasks, newTask]);
      sendMessage({ type: 'task-update', action: 'create', taskId: newTask.id });
      setError(null);
    } catch (err) {
      setError('Failed to create task');
      console.error(err);
    }
  };

  const handleDeleteTask = async (id: string) => {
    try {
      await taskApi.deleteTask(id);
      setTasks(tasks.filter((task) => task.id !== id));
      sendMessage({ type: 'task-update', action: 'delete', taskId: id });
      setError(null);
    } catch (err) {
      setError('Failed to delete task');
      console.error(err);
    }
  };

  const handleStatusChange = async (id: string, status: Task['status']) => {
    try {
      const updatedTask = await taskApi.updateTask(id, { status });
      setTasks(tasks.map((task) => (task.id === id ? updatedTask : task)));
      sendMessage({ type: 'task-update', action: 'update', taskId: id });
      setError(null);
    } catch (err) {
      setError('Failed to update task');
      console.error(err);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      <div className="container mx-auto px-4 py-8">
        <div className="flex justify-between items-center mb-8">
          <div>
            <h1 className="text-4xl font-bold text-gray-800 mb-2">TaskBoard</h1>
            <p className="text-gray-600">Real-time collaborative task management</p>
          </div>
          <div className="flex items-center gap-4">
            <div className="flex items-center gap-2">
              <div
                className={`w-3 h-3 rounded-full ${
                  isConnected ? 'bg-green-500' : 'bg-red-500'
                }`}
              ></div>
              <span className="text-sm text-gray-600">
                {isConnected ? 'Connected' : 'Disconnected'}
              </span>
            </div>
            <button
              onClick={() => setIsModalOpen(true)}
              className="px-6 py-3 bg-blue-500 text-white rounded-lg hover:bg-blue-600 font-semibold shadow-lg transition-all"
            >
              + Add Task
            </button>
          </div>
        </div>

        {error && (
          <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
            {error}
          </div>
        )}

        <div className="flex gap-6 overflow-x-auto pb-4">
          <TaskColumn
            title="To Do"
            status="todo"
            tasks={tasks}
            onDelete={handleDeleteTask}
            onStatusChange={handleStatusChange}
          />
          <TaskColumn
            title="In Progress"
            status="in-progress"
            tasks={tasks}
            onDelete={handleDeleteTask}
            onStatusChange={handleStatusChange}
          />
          <TaskColumn
            title="Done"
            status="done"
            tasks={tasks}
            onDelete={handleDeleteTask}
            onStatusChange={handleStatusChange}
          />
        </div>
      </div>

      <AddTaskModal isOpen={isModalOpen} onClose={() => setIsModalOpen(false)} onAdd={handleAddTask} />
    </div>
  );
}

export default App;
