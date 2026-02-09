# Bug Report

### Describe the bug

After a recent update, the `meta()` method behavior has changed and is now returning cached values even when the underlying object properties are modified. The cache doesn't invalidate properly when properties change, causing stale metadata to be returned.

### Reproduction

```js
const property = new PropertyBase('test');

// First call returns metadata
const meta1 = property.meta();

// Modify the object in some way
// (e.g., add properties, change internal state)

// Second call returns the same cached metadata
const meta2 = property.meta();

// meta2 should reflect the changes but it's still the old cached version
```

### Expected behavior

The `meta()` method should return up-to-date metadata that reflects the current state of the object. If caching is being used, it should invalidate automatically when the object changes, or there should be a clear way to force cache invalidation.

### Additional context

This seems to have started after some refactoring of the PropertyBase class. The old implementation would recompute metadata on each call, but now it appears to be using a caching mechanism (`_metaCache` and `_metaCacheDirty` flags) that doesn't properly invalidate when needed.

---
Repository: /testbed
