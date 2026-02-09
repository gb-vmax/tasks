# Bug Report

### Describe the bug

I'm experiencing an issue with path tracking in the AST utilities. When tracking entities with discriminated paths, the behavior seems inverted - entities that should be marked as already tracked are being treated as new, and vice versa.

### Reproduction

```js
const tracker = new DiscriminatedPathTracker();
const entity = { id: 1 };
const path = ['root', 'nested', 'property'];
const discriminator = 'type';

// First call should return false (entity is new)
const firstResult = tracker.track(path, discriminator, entity);
console.log(firstResult); // Expected: false, but getting true

// Second call with same entity should return true (already tracked)
const secondResult = tracker.track(path, discriminator, entity);
console.log(secondResult); // Expected: true, but getting false
```

### Expected behavior

- First time tracking an entity: should return `false` (entity is new, not previously tracked)
- Subsequent calls with the same entity: should return `true` (entity was already tracked)

The return values appear to be inverted from what they should be.

### Additional context

This is affecting how the tracker determines whether an entity has already been processed, which could lead to duplicate processing or skipped entities in the AST traversal.

---
Repository: /testbed
