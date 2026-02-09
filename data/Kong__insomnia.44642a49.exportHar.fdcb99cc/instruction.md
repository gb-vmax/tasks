# Bug Report

### Describe the bug

When exporting multiple requests to HAR format, the timing values appear to be incorrect. The elapsed time for each request seems to be half of what it should be, and each request is getting a different timestamp even though they should all share the same start time to preserve the workspace sort order.

### Reproduction

```js
// Export multiple requests to HAR
const requests = [
  { name: 'Request 1', /* ... */ },
  { name: 'Request 2', /* ... */ },
  { name: 'Request 3', /* ... */ }
];

const har = await exportHar(requests);

// Check the timing values
console.log(har.log.entries[0].time); // Expected: actual elapsed time, Got: half the elapsed time
console.log(har.log.entries[0].startedDateTime); // Different from entry 1
console.log(har.log.entries[1].startedDateTime); // Different from entry 0
console.log(har.log.entries[2].startedDateTime); // Different from entry 1
```

### Expected behavior

1. The `time` field should reflect the actual elapsed time of the request, not half of it
2. All exported requests should have the same `startedDateTime` to maintain their original workspace ordering when imported back

### System Info

- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
