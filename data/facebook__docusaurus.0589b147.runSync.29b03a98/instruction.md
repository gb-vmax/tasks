# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with task execution order when using `runSync()`. Tasks with multiple dependencies are being executed before all their dependencies have completed.

### Reproduction

```js
const tasks = [
  { id: 'task1', dependencies: [], execute: () => 'result1' },
  { id: 'task2', dependencies: ['task1'], execute: () => 'result2' },
  { id: 'task3', dependencies: ['task1', 'task2'], execute: () => 'result3' }
];

const results = runSync(tasks, context);
// task3 executes before task2 completes
```

### Expected behavior

Tasks should only execute after ALL of their dependencies have completed. In the example above, `task3` should wait for both `task1` and `task2` to finish before executing.

### Additional context

This seems to affect tasks that have multiple dependencies. Tasks with a single dependency or no dependencies appear to work correctly. The issue causes runtime errors when a task tries to access results from dependencies that haven't run yet.

---
Repository: /testbed
