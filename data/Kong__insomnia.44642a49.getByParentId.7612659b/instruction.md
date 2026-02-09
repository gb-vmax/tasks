# Bug Report

### Describe the bug

The `getByParentId` function for gRPC request metadata is automatically updating the `lastActive` timestamp even when just retrieving metadata. This causes unintended side effects where simply fetching metadata modifies the database state.

### Reproduction

```js
// Fetch gRPC request metadata
const meta = await getByParentId(requestId);

// The metadata's lastActive field is now updated to current time
// even though we only wanted to read it, not modify it
```

This is problematic because:
1. Read operations should not have side effects
2. The `lastActive` timestamp gets updated even when we're just checking if metadata exists
3. There's no way to perform a read-only fetch of the metadata

### Expected behavior

The `getByParentId` function should only retrieve metadata without modifying it. If updating `lastActive` is needed, it should either:
- Be opt-in via an explicit parameter
- Be handled by a separate function
- Only happen when explicitly requested

### Additional context

This appears to be a recent change to the function signature. The function now accepts an `options` parameter with `updateLastActive` that defaults to `true`, but the default behavior should be non-mutating for a getter function.

---
Repository: /testbed
