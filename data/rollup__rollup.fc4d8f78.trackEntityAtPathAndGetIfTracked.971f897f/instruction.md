# Bug Report

### Describe the bug

I'm experiencing an issue with path tracking where entities are not being tracked correctly at nested paths. When I try to track an entity at a specific path, the behavior seems inverted - it returns `true` when the entity was already tracked (should return `false`) and `false` when it's newly tracked (should return `true`).

Additionally, there seems to be a problem with how deeply nested paths are traversed. The last segment of the path appears to be skipped, causing entities to be tracked at the wrong level.

### Reproduction

```js
const tracker = new DiscriminatedPathTracker();

// Track an entity at a path
const path = ['a', 'b', 'c'];
const result1 = tracker.trackEntityAtPathAndGetIfTracked(path, 'discriminator', entityObj);
// Expected: false (newly tracked)
// Actual: true

// Track the same entity again
const result2 = tracker.trackEntityAtPathAndGetIfTracked(path, 'discriminator', entityObj);
// Expected: true (already tracked)
// Actual: false

// Also, the entity seems to be tracked at path ['a', 'b'] instead of ['a', 'b', 'c']
```

### Expected behavior

1. `trackEntityAtPathAndGetIfTracked` should return `false` when tracking a new entity
2. It should return `true` when the entity was already tracked at that path
3. The entity should be tracked at the complete path, not one level above

This is breaking functionality that depends on knowing whether an entity was previously tracked.

---
Repository: /testbed
