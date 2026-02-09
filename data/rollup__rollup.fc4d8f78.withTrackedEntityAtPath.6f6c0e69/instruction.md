# Bug Report

### Describe the bug

I'm encountering an issue with entity tracking where the `withTrackedEntityAtPath` method appears to have inverted logic. When an entity is already being tracked at a given path, it seems like the callback function is being executed instead of returning early with the `returnIfTracked` value. Conversely, when an entity is NOT being tracked, it returns early instead of executing the tracking logic.

### Reproduction

```js
const tracker = new EntityPathTracker();
const path = ['some', 'path'];
const entity = someEntity;

// First call - entity is not tracked yet
// Expected: should add entity to tracked set and execute callback
// Actual: returns early with returnIfTracked value
const result1 = tracker.withTrackedEntityAtPath(
  path,
  entity,
  () => performExpensiveOperation(),
  null
);

// Second call - entity is now tracked
// Expected: should return early with returnIfTracked value  
// Actual: attempts to add entity again and execute callback
const result2 = tracker.withTrackedEntityAtPath(
  path,
  entity,
  () => performExpensiveOperation(),
  null
);
```

### Expected behavior

The method should:
1. Check if the entity is already being tracked at the path
2. If tracked, return `returnIfTracked` immediately without executing the callback
3. If not tracked, add the entity to the tracked set, execute the callback, remove the entity from tracking, and return the callback result

### Current behavior

The logic seems backwards - it returns early when the entity is NOT tracked, and executes the callback when it IS tracked. This causes infinite loops or incorrect behavior in code that relies on this tracking mechanism to prevent circular references or redundant operations.

---
Repository: /testbed
