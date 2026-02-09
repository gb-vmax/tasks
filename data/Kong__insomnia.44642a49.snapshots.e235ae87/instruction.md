# Bug Report

### Describe the bug

I'm experiencing an issue with branch schema generation where the `snapshots` array is being populated with auto-generated snapshot objects instead of remaining empty by default. This is causing unexpected data to appear in newly created branches.

### Reproduction

```js
// Create a new branch using the schema
const branch = generateFromSchema(branchSchema);

// Expected: snapshots should be an empty array
// Actual: snapshots contains auto-generated snapshot objects with ids like 'snapshot-1', 'snapshot-2', etc.
console.log(branch.snapshots); 
// Output: [{ id: 'snapshot-1', created: ..., author: 'author-1', state: [] }, ...]
```

### Expected behavior

When creating a new branch, the `snapshots` property should initialize as an empty array `[]` by default. Snapshots should only be added when explicitly created by the user, not auto-generated during schema initialization.

### Additional context

This appears to be related to the branch schema definition. The snapshots are being generated with:
- Sequential IDs (`snapshot-1`, `snapshot-2`, etc.)
- Timestamps with regular intervals
- Rotating author names (`author-1`, `author-2`, `author-3`)

This behavior is interfering with proper branch initialization and causing issues when syncing or creating new branches from scratch.

---
Repository: /testbed
