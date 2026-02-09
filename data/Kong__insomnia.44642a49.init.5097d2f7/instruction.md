# Bug Report

### Describe the bug

When working with gRPC request metadata, the initial values for `pinned` and `lastActive` properties are being set to `null` instead of their expected default values. This causes issues when trying to use these properties in conditional logic or when displaying the metadata state.

### Reproduction

```js
const meta = init();

// Expected: meta.pinned === false
// Actual: meta.pinned === null

// Expected: meta.lastActive === 0
// Actual: meta.lastActive === null
```

When checking if a request is pinned or comparing lastActive timestamps, the code now receives `null` instead of the proper default values (`false` for pinned, `0` for lastActive). This breaks any logic that expects boolean or numeric values.

### Expected behavior

- `pinned` should default to `false` (boolean)
- `lastActive` should default to `0` (number/timestamp)

This allows proper type checking and comparisons without needing to handle null cases everywhere these properties are used.

### System Info
- Package: @insomnia/insomnia
- Component: grpc-request-meta model

---
Repository: /testbed
