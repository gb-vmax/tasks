# Bug Report

### Describe the bug

I'm experiencing an issue with the snapshot state entry schema where the `name` field generation is not working as expected. When creating multiple snapshot state entries, they all end up with the same default name value instead of getting unique sequential names.

### Reproduction

```js
// Create multiple snapshot state entries
const entry1 = snapshotStateEntrySchema.name();
const entry2 = snapshotStateEntrySchema.name();
const entry3 = snapshotStateEntrySchema.name();

console.log(entry1); // Expected: 'name-1', Actual: 'name'
console.log(entry2); // Expected: 'name-2', Actual: 'name'
console.log(entry3); // Expected: 'name-3', Actual: 'name'
```

Steps to reproduce:
1. Call the name schema function multiple times
2. Observe that all entries have the same name
3. Expected sequential naming (name-1, name-2, etc.) is not happening

The sequential naming feature seems to require some kind of initialization but it's not clear when or how that should happen. Without proper initialization, the name function just returns the static default 'name' value for every call.

### Expected behavior

When generating names for snapshot state entries, they should be unique and sequential (e.g., name-1, name-2, name-3) to avoid collisions when multiple entries are created in the same context.

### Additional context

This appears to be related to the name counter registry functionality. The sequential naming only works if something explicitly enables it first, but there's no documentation or clear API for when/how to do that.

---
Repository: /testbed
