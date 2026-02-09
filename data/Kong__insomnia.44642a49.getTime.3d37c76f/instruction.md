# Bug Report

### Describe the bug

When using the plugin context API to get response timing information, `response.getTime()` returns `0` instead of `null` when the elapsed time is not available. This causes issues when trying to distinguish between a response that took 0ms and a response where timing information is unavailable.

### Reproduction

```js
// In a plugin script
const response = context.response;

// When response has no timing data
const time = response.getTime();
console.log(time); // Expected: null, Actual: 0

// This makes it impossible to check if timing is available:
if (time === 0) {
  // Could be either "no timing data" OR "request took 0ms"
}
```

### Expected behavior

`response.getTime()` should return `null` when timing information is not available, rather than `0`. This would allow proper checking for the presence of timing data:

```js
const time = response.getTime();
if (time === null) {
  // Timing not available
} else if (time === 0) {
  // Request actually took 0ms
}
```

### System Info
- Insomnia version: latest
- Platform: macOS

---
Repository: /testbed
