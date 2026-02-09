# Bug Report

### Describe the bug

I'm experiencing an issue with error handling in the watch task where modules are being incorrectly filtered from the cache when an error occurs. After an error is thrown during the build process, the wrong modules remain in the cache, causing subsequent builds to fail or behave unexpectedly.

### Reproduction

```js
// Trigger a build error with a specific module ID
// The error object contains an id property

// After the error is handled:
// - The module that caused the error is still in cache
// - Other unrelated modules are removed from cache instead
```

Steps to reproduce:
1. Set up a watch task with multiple cached modules
2. Introduce an error in one specific module (error will have an `id` property)
3. Observe that after error handling, the erroring module remains in cache
4. Other modules that should be kept are incorrectly removed

### Expected behavior

When an error occurs with a specific module ID, that module should be removed from the cache. Other modules should remain untouched. Currently it seems like the opposite is happening - the problematic module stays while others are filtered out.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
