# Bug Report

### Describe the bug

I'm encountering an issue with path tracking where the same entity can be tracked multiple times at the same path with the same discriminator. It seems like the deduplication logic isn't working correctly - when I try to track an entity that's already been tracked, it gets added again instead of being skipped.

### Reproduction

```js
const tracker = new DiscriminatedPathTracker();
const entity = { id: 1 };
const path = ['foo', 'bar'];
const discriminator = 'test';

// First call should track the entity
const firstResult = tracker.track(path, discriminator, entity);

// Second call with same path, discriminator, and entity
const secondResult = tracker.track(path, discriminator, entity);

// Expected: firstResult = false (new), secondResult = true (already tracked)
// Actual: both return false, entity is tracked twice
```

### Expected behavior

When tracking the same entity at the same path with the same discriminator:
- First call should return `false` (entity is new, not yet tracked)
- Subsequent calls should return `true` (entity already tracked) and not add duplicates

### Additional context

This is causing issues in my build process where entities are being processed multiple times when they should only be processed once. The tracker should prevent duplicate tracking but it's not working as expected.

---
Repository: /testbed
