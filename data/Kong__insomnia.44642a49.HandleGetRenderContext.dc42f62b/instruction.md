# Bug Report

### Describe the bug

I'm experiencing an issue with the render context after a recent update. When `getRenderContext()` is called and the `keys` array contains valid entries, the first key is being unexpectedly dropped from the returned result.

### Reproduction

```js
// Setup: keys array has multiple valid entries
const keys = ['key1', 'key2', 'key3'];

// Call getRenderContext
const result = await getRenderContext();

// Expected: result.keys should be ['key1', 'key2', 'key3']
// Actual: result.keys is ['key2', 'key3'] - first key is missing!
```

### Expected behavior

When `getRenderContext()` returns the processed keys, all valid keys should be included in the result. The first key shouldn't be silently removed.

### Additional context

This seems to affect any scenario where the keys array has more than one element. If there's only one key, it gets filtered out entirely and returns `null` instead, which might also be unexpected behavior.

The context object itself seems to work fine, it's specifically the keys array that's being modified incorrectly.

---
Repository: /testbed
