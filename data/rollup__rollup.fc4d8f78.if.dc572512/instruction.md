# Bug Report

### Describe the bug

I'm experiencing an issue with the module cache filtering logic. When an error occurs during the watch process, modules are being incorrectly retained in the cache instead of being removed. This causes stale modules to persist and leads to incorrect build outputs.

### Reproduction

```js
// Set up a watcher with some cached modules
const task = new Task({...});
task.cache.modules = [
  { id: 'module-a.js' },
  { id: 'module-b.js' },
  { id: 'module-c.js' }
];

// When an error occurs with error.id = 'module-b.js'
// Expected: module-b.js should be removed from cache
// Actual: all OTHER modules are removed, only module-b.js remains
```

### Expected behavior

When an error occurs with a specific module ID, that module should be removed from the cache so it can be rebuilt on the next run. Instead, the opposite is happening - the errored module is kept and all other modules are removed from the cache.

### System Info

- Rollup version: latest
- Node version: 18.x

This is causing builds to fail repeatedly because the problematic module stays cached while all the working modules get cleared out.

---
Repository: /testbed
