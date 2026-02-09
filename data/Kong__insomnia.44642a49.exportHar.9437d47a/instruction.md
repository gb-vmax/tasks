# Bug Report

### Describe the bug

When exporting HAR files, the timing information for responses is showing incorrect values. The `wait` timing is always being set to 0 when a response exists, instead of using the actual elapsed time from the response.

### Reproduction

```js
// Export a request that has a response with elapsed time
const exportRequest = {
  requestId: 'req_123',
  responseId: 'res_456',
  environmentId: 'env_789'
}

// The response has elapsedTime = 250ms
const response = {
  elapsedTime: 250
}

// After export, the HAR timings show:
{
  timings: {
    wait: 0  // Should be 250
  }
}
```

### Expected behavior

The `wait` timing in the exported HAR file should reflect the actual `elapsedTime` from the response object (e.g., 250ms), not 0.

### Additional context

This appears to affect all HAR exports where a response exists. The timing data is being inverted - it's set to 0 when a response is present, but would use `elapsedTime` when no response exists (which doesn't make sense).

---
Repository: /testbed
