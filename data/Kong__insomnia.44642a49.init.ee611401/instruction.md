# Bug Report

### Describe the bug

When creating a new gRPC request metadata object using the `init()` function, the `lastActive` timestamp is being set to the current time instead of 0. This causes newly created requests to appear as if they were recently accessed, which affects sorting and filtering behavior.

### Reproduction

```js
const meta = init();
console.log(meta.lastActive); // Expected: 0, Actual: current timestamp
```

The issue appears when:
1. Creating a new gRPC request
2. The metadata is initialized with `init()`
3. `lastActive` should be 0 for a brand new request that hasn't been accessed yet
4. Instead it's set to `Date.now()`

This breaks any logic that relies on `lastActive: 0` to identify requests that have never been accessed. For example, sorting by "recently used" now incorrectly includes brand new requests at the top of the list.

### Expected behavior

New gRPC request metadata should have `lastActive` set to 0 to indicate the request has never been accessed. The timestamp should only be updated when the request is actually opened or used.

---
Repository: /testbed
