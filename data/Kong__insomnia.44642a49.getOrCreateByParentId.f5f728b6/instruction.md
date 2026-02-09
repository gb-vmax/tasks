# Bug Report

### Describe the bug

When calling `getOrCreateByParentId()` multiple times in quick succession for the same parent ID, the `lastActive` timestamp is not being updated consistently. The function returns the existing request meta without refreshing the `lastActive` field, which causes issues with tracking when a gRPC request was last accessed.

### Reproduction

```js
const parentId = 'test-parent-id';

// First call creates the request meta
const meta1 = await getOrCreateByParentId(parentId);
console.log('First call lastActive:', meta1.lastActive);

// Wait a moment
await new Promise(resolve => setTimeout(resolve, 100));

// Second call should update lastActive but doesn't
const meta2 = await getOrCreateByParentId(parentId);
console.log('Second call lastActive:', meta2.lastActive);

// Expected: meta2.lastActive should be newer than meta1.lastActive
// Actual: Both timestamps are identical
```

### Expected behavior

Each call to `getOrCreateByParentId()` should update the `lastActive` timestamp to reflect the current time, ensuring that the most recent access time is always tracked. This is important for features that rely on knowing when a gRPC request was last used.

### Additional context

This affects the accuracy of "recently used" features and any logic that depends on the `lastActive` timestamp being current. The function should always return request meta with an up-to-date `lastActive` value.

---
Repository: /testbed
