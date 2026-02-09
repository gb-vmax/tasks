# Bug Report

### Describe the bug

I'm experiencing an issue with entity tracking in nested paths. When attempting to track an entity at a specific path, the tracking logic appears to be inverted - entities that should be tracked are being skipped, and entities that should be skipped are being processed.

### Reproduction

```js
const tracker = new EntityPathTracker();
const path = ['some', 'nested', 'path'];
const entity = someEntity;

// First call - entity is not yet tracked
const result1 = tracker.withTrackedEntityAtPath(
  path,
  entity,
  () => processEntity(),
  'already-tracked'
);
// Expected: processEntity() to be called and return its result
// Actual: returns 'already-tracked' immediately

// Second call - entity should now be tracked
const result2 = tracker.withTrackedEntityAtPath(
  path,
  entity,
  () => processEntity(),
  'already-tracked'
);
// Expected: returns 'already-tracked' immediately
// Actual: processEntity() gets called again
```

### Expected behavior

The method should:
1. Check if an entity is already being tracked at the given path
2. If tracked, return the `returnIfTracked` value immediately
3. If not tracked, add it to tracking, execute `onUntracked()`, remove from tracking, and return the result

Currently it seems to be doing the opposite - returning early when the entity is NOT tracked, and processing when it IS tracked.

### Additional context

This is causing infinite loops in my code because entities keep getting reprocessed when they should be skipped. The tracking mechanism seems completely backwards from what it should be doing.

---
Repository: /testbed
