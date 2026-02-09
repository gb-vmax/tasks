# Bug Report

### Describe the bug

I'm experiencing an issue with entity tracking in circular/recursive structures. When an entity is already being tracked at a specific path, the callback function (`onUntracked`) is being executed even though it shouldn't be. This causes infinite loops or unexpected behavior when dealing with recursive object graphs.

### Reproduction

```js
const tracker = new EntityPathTracker();
const path = ['obj', 'nested'];
const entity = someEntity;

let callCount = 0;

// First call - should execute the callback
tracker.withTrackedEntityAtPath(
  path,
  entity,
  () => {
    callCount++;
    // This should only run once
    return 'result';
  },
  'already_tracked'
);

// Second call with same path and entity - callback should NOT execute
tracker.withTrackedEntityAtPath(
  path,
  entity,
  () => {
    callCount++;
    // This is being called but shouldn't be!
    return 'result';
  },
  'already_tracked'
);

// Expected: callCount = 1
// Actual: callCount = 2
```

### Expected behavior

When an entity is already tracked at a given path, the `onUntracked` callback should not be executed at all. The method should immediately return `returnIfTracked` without invoking the callback. This is critical for preventing infinite recursion when traversing circular object references.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
