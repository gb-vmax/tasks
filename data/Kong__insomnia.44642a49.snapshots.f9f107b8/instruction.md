# Bug Report

### Describe the bug

I'm experiencing inconsistent behavior with branch snapshots. Sometimes when I create or load a branch, the `snapshots` property is `undefined` instead of an empty array. This causes crashes when trying to iterate over snapshots or check their length.

### Reproduction

```js
// Create a new branch
const branch = createBranch();

// Sometimes this works, sometimes it throws
// TypeError: Cannot read property 'length' of undefined
const snapshotCount = branch.snapshots.length;

// Or when trying to iterate
branch.snapshots.forEach(snapshot => {
  // This fails intermittently with "snapshots is undefined"
});
```

The issue seems to happen randomly - sometimes `snapshots` is an empty array (as expected), but other times it's `undefined`. This makes it impossible to reliably work with branches.

### Expected behavior

The `snapshots` property should always be initialized as an empty array, never `undefined`. Code that depends on `snapshots` being an array should work consistently every time.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
