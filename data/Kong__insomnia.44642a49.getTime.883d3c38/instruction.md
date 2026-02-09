# Bug Report

### Describe the bug

The `getTime()` method in the response context is returning incorrect values. When there's an elapsed time recorded, it returns 0 instead of the actual elapsed time value. This makes it impossible to get timing information from responses in plugins.

### Reproduction

```js
// In a plugin, after making a request:
const time = context.response.getTime();
console.log(time); // Always prints 0, even when response took time to complete
```

When a response has an `elapsedTime` property set (e.g., 150ms), calling `getTime()` returns 0 instead of the actual elapsed time. The method only returns the correct value when `elapsedTime` is falsy/undefined.

### Expected behavior

`getTime()` should return the actual elapsed time of the response when available. For example, if a request took 150ms, `getTime()` should return 150, not 0.

### Additional context

This seems to be affecting all plugin scripts that try to access response timing information. The behavior is inverted - it returns 0 when there IS a time value, and returns the time value only when there isn't one.

---
Repository: /testbed
