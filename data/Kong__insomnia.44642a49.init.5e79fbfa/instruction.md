# Bug Report

### Describe the bug

After a recent update, newly created gRPC requests have unexpected default values. The `metaSortKey` is now positive instead of negative, and reflection API is enabled by default when it should be disabled.

### Reproduction

```js
// Create a new gRPC request
const grpcRequest = init();

// Check the default values
console.log(grpcRequest.metaSortKey); // Expected: negative timestamp, Actual: positive timestamp
console.log(grpcRequest.reflectionApi.enabled); // Expected: false, Actual: true
```

### Expected behavior

When initializing a new gRPC request:
- `metaSortKey` should be `-1 * Date.now()` (negative value) for proper sorting
- `reflectionApi.enabled` should default to `false`

### System Info
- Insomnia version: latest
- Platform: All platforms

This is causing issues with request ordering in the sidebar and unexpected reflection API behavior on new requests.

---
Repository: /testbed
