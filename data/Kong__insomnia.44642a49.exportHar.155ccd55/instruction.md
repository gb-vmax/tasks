# Bug Report

### Describe the bug

I'm experiencing an issue with HAR exports where the order of requests appears to be reversed compared to what I expected. When I export multiple requests to HAR format, they seem to be in the opposite order from how they were provided.

Additionally, the timing information in the exported HAR file looks incorrect - the `wait` time values are showing up as half of what they should be based on the actual response elapsed times.

### Reproduction

```js
// Export multiple requests in a specific order
const requests = [
  { requestId: 'req1', ... },
  { requestId: 'req2', ... },
  { requestId: 'req3', ... }
];

const har = await exportHar(requests);

// The entries in har.log.entries are in reverse order (req3, req2, req1)
// Also, if a response took 100ms, the wait time shows 50ms instead
```

### Expected behavior

1. Requests should appear in the HAR export in the same order they were provided
2. The `wait` timing should match the actual response elapsed time, not half of it

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
