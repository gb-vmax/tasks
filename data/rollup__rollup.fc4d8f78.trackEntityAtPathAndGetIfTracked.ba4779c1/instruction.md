# Bug Report

### Describe the bug

I'm experiencing an issue with path tracking where entities are being tracked multiple times even when they've already been tracked at the same path with the same discriminator. The tracking function seems to always return `true` on the first call, even for entities that haven't been seen before.

### Reproduction

```js
const tracker = new DiscriminatedPathTracker();
const path = ['user', 'profile'];
const discriminator = 'someKey';
const entity = { id: 1 };

// First call - should return false (not tracked yet)
const firstResult = tracker.trackEntityAtPathAndGetIfTracked(path, discriminator, entity);
console.log(firstResult); // Expected: false, Actual: true

// Second call - should return true (already tracked)
const secondResult = tracker.trackEntityAtPathAndGetIfTracked(path, discriminator, entity);
console.log(secondResult); // Expected: true, Actual: true
```

### Expected behavior

The first call to `trackEntityAtPathAndGetIfTracked` should return `false` since the entity hasn't been tracked yet. Only subsequent calls with the same entity, path, and discriminator should return `true`.

The function should:
1. Check if the entity is already tracked
2. If not tracked, add it and return `false`
3. If already tracked, return `true`

Currently it seems to be adding the entity before checking if it was already present, causing the check to always succeed.

---
Repository: /testbed
