# Bug Report

### Describe the bug

I'm experiencing inconsistent behavior with merge conflict resolution in the sync module. Sometimes the `mineBlob` property returns `null` when it should contain a blob hash, but other times it returns a hash value. This seems to happen randomly and is making merge conflict resolution unreliable.

### Reproduction

```js
const conflict = {
  key: () => 'my-conflict-key',
  choose: () => null,
  // ... other properties
}

// Sometimes mineBlob returns null
const blob1 = mergeConflictSchema.mineBlob.call(conflict)
console.log(blob1) // null (unexpected)

// Using a different key might return a hash
const conflict2 = {
  key: () => 'another-key',
  choose: () => null,
}
const blob2 = mergeConflictSchema.mineBlob.call(conflict2)
console.log(blob2) // returns a hash string
```

### Expected behavior

The `mineBlob` should consistently return either a blob hash or `null` based on clear, deterministic logic. Right now it appears to be non-deterministic which makes it impossible to reliably handle merge conflicts.

### Additional context

This is causing issues when trying to resolve merge conflicts during sync operations. Some conflicts can't be properly resolved because the blob information is missing unexpectedly.

---
Repository: /testbed
