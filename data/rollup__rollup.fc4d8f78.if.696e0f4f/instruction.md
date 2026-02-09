# Bug Report

### Describe the bug

I'm experiencing an issue where modules are not being properly removed from the cache when errors occur during the build process. After an error is thrown with an `error.id`, the problematic module remains in the cache instead of being cleared out.

### Reproduction

```js
// When a build error occurs with error.id set
// The module should be removed from cache but isn't

const task = new Task(/* ... */);
// Trigger an error during build that includes error.id
// Expected: module with error.id is removed from cache
// Actual: module with error.id remains in cache
```

### Steps to reproduce:
1. Set up a build task with cached modules
2. Trigger a build error that includes an `error.id` property
3. Check the cache.modules array
4. The module that caused the error is still present in the cache

### Expected behavior

When an error occurs with an `error.id`, the module associated with that ID should be filtered out and removed from `cache.modules`. This would allow the build to properly recover and re-process the problematic module on the next attempt.

### Actual behavior

The module remains in the cache, which can cause stale or incorrect modules to persist across build attempts.

---
Repository: /testbed
