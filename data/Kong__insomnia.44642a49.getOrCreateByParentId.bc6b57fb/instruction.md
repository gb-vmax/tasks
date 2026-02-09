# Bug Report

### Describe the bug

After a recent update, I'm noticing that `getOrCreateByParentId` is updating the `lastActive` timestamp on every call, even when called in quick succession. This is causing unnecessary database writes and performance issues when the function is called repeatedly within short time intervals.

### Reproduction

```js
const meta1 = await getOrCreateByParentId('test-parent-id');
console.log(meta1.lastActive); // e.g., 1234567890000

// Call again immediately
const meta2 = await getOrCreateByParentId('test-parent-id');
console.log(meta2.lastActive); // e.g., 1234567890100 - different timestamp!

// The lastActive field keeps changing even though only 100ms passed
```

### Expected behavior

The `lastActive` timestamp should only be updated if a certain threshold has passed (e.g., 5 seconds), not on every single call. Calling `getOrCreateByParentId` multiple times in quick succession should return the same metadata object without triggering database updates.

### Additional context

This is causing performance problems in our application where we call this function frequently during gRPC request handling. The constant database writes are unnecessary and slow things down.

---
Repository: /testbed
