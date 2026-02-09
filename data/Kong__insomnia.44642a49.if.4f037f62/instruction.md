# Bug Report

### Describe the bug

When handling responses without a body or bodyPath, the `getBodyBuffer` function is returning an incorrect buffer size. Instead of returning an empty buffer (size 0), it's now returning a buffer with size 1, which causes issues when processing empty response bodies.

### Reproduction

```js
const response = {
  // No bodyPath defined
};

const buffer = getBodyBuffer(response);
console.log(buffer.length); // Expected: 0, Actual: 1
```

Or when response is null/undefined:

```js
const buffer = getBodyBuffer(null);
console.log(buffer.length); // Expected: 0, Actual: 1
```

### Expected behavior

When a response has no body or no bodyPath, `getBodyBuffer` should return an empty buffer with length 0, not a buffer with length 1. This is important for correctly identifying empty responses and avoiding issues with downstream processing that expects truly empty buffers.

### Additional context

This seems to have changed recently and is affecting response handling logic that relies on checking buffer length to determine if a response has content.

---
Repository: /testbed
