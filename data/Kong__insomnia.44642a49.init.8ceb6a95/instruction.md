# Bug Report

### Describe the bug

When creating new gRPC request metadata, the `lastActive` timestamp is being set to the current time instead of initializing to 0. This is causing issues with sorting and filtering logic that expects newly created requests to have a `lastActive` value of 0 until they are actually used.

### Reproduction

```js
// Create a new gRPC request meta
const meta = init();

console.log(meta.lastActive); // Expected: 0, Actual: current timestamp (e.g., 1703001234567)
```

The problem is that `lastActive` should only be set when the request is actually accessed or used, not during initialization. This breaks workflows that rely on distinguishing between "never accessed" (0) and "recently accessed" requests.

### Expected behavior

- `lastActive` should be initialized to `0` for new gRPC request metadata
- The timestamp should only be updated when the request is actually used/accessed
- This allows proper sorting of requests by activity (new requests should appear separately from recently used ones)

### Additional context

This seems to have changed recently. Previously, new requests would correctly show `lastActive: 0` until they were actually opened or executed. Now they immediately get a timestamp, making it impossible to tell which requests are truly new vs. which have been used.

---
Repository: /testbed
