# Bug Report

### Describe the bug

I'm experiencing an issue with entity tracking in nested object paths. When tracking entities at specific paths, the tracking logic seems to be inverted - entities that should be tracked are being skipped, and entities that shouldn't be tracked are being processed.

### Reproduction

```js
const tracker = new EntityPathTracker();
const path = ['obj', 'nested', 'prop'];
const entity = someEntity;

// First call - entity is not yet tracked, should execute callback
const result1 = tracker.withTrackedEntityAtPath(
  path,
  entity,
  () => processEntity(),
  'already-tracked'
);

// Expected: processEntity() is called and entity gets tracked
// Actual: Returns 'already-tracked' immediately without processing

// Second call - entity is now tracked, should skip
const result2 = tracker.withTrackedEntityAtPath(
  path,
  entity,
  () => processEntity(),
  'already-tracked'
);

// Expected: Returns 'already-tracked' without calling processEntity()
// Actual: Calls processEntity() again
```

### Expected behavior

The `withTrackedEntityAtPath` method should:
1. Check if an entity is already tracked at the given path
2. If tracked, return the `returnIfTracked` value immediately
3. If not tracked, add it to the tracked set, execute the callback, then remove it from the set

Instead, it appears to be doing the opposite - returning early when the entity is NOT tracked, and processing when it IS tracked.

### System Info
- Rollup version: Latest
- Node version: 18.x

This is causing infinite loops in my build process where entities keep getting reprocessed when they should be skipped.

---
Repository: /testbed
