# Bug Report

### Describe the bug

I'm encountering an issue with path tracking where entities are being tracked incorrectly. When I try to track the same entity multiple times with the same discriminator, the tracker returns the wrong boolean value indicating whether the entity was already tracked.

### Reproduction

```js
const tracker = new DiscriminatedPathTracker();

// First time tracking an entity
const isNew1 = tracker.trackEntityAtPathAndGetIfTracked(['path'], 'discriminator', entityObject);
console.log(isNew1); // Expected: true (first time seeing this entity)

// Second time tracking the same entity
const isNew2 = tracker.trackEntityAtPathAndGetIfTracked(['path'], 'discriminator', entityObject);
console.log(isNew2); // Expected: false (already tracked)

// But the actual behavior is inverted - returns false on first track, true on subsequent tracks
```

### Expected behavior

The method should return `true` when an entity is tracked for the first time (newly added) and `false` when it's already been tracked before. Currently it seems to be doing the opposite.

### Additional context

This is affecting my code that relies on knowing whether an entity has been seen before during path traversal. The inverted return values are causing incorrect behavior in my analysis logic.

---
Repository: /testbed
