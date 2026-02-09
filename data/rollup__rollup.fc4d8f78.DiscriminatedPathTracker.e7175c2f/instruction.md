# Bug Report

### Describe the bug

I'm experiencing an issue with the path tracking system where entities are being tracked incorrectly. It seems like the tracker is reporting the opposite of what it should - when an entity is already tracked, it returns `false`, and when it's newly tracked, it returns `true`. This is causing problems with duplicate tracking detection in my code.

### Reproduction

```js
const tracker = new DiscriminatedPathTracker();
const entity = { id: 1 };
const discriminator = 'myPath';

// First call should return false (entity not previously tracked)
const firstResult = tracker.track(entity, discriminator);
console.log('First track:', firstResult); // Expected: false, but getting true

// Second call should return true (entity already tracked)
const secondResult = tracker.track(entity, discriminator);
console.log('Second track:', secondResult); // Expected: true, but getting false
```

### Expected behavior

The `track()` method should return `false` when tracking an entity for the first time, and `true` when the entity has already been tracked. Currently it appears to be returning the inverse.

This is breaking logic that depends on knowing whether an entity was already being tracked or not.

### System Info
- Latest version from main branch
- Node.js 18.x

---
Repository: /testbed
