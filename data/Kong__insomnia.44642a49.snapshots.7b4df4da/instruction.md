# Bug Report

### Describe the bug

After a recent update, the branch schema is generating snapshot data based on an environment variable `FLUENT_BUILDER_SNAPSHOT_COUNT`. This is causing issues when the environment variable is set, as branches are being initialized with unexpected snapshot entries instead of empty arrays.

### Reproduction

```js
// Set environment variable
process.env.FLUENT_BUILDER_SNAPSHOT_COUNT = '3';

// Create a new branch using the schema
const branch = createBranch(); // or however branches are initialized

console.log(branch.snapshots);
// Expected: []
// Actual: Array with 3 snapshot entries including IDs, blobs, authors, etc.
```

The snapshots array should be empty by default, but instead it contains generated snapshot data with:
- Auto-generated snapshot IDs
- Blob references
- Author information
- State arrays with keys and resource names
- Parent relationships between snapshots

### Expected behavior

New branches should initialize with an empty snapshots array (`[]`) regardless of environment variables. The schema default should not be affected by external configuration.

### System Info
- Package: @insomnia/sync
- Node version: 18.x

This seems like it might be test/development code that accidentally got included in the schema defaults?

---
Repository: /testbed
