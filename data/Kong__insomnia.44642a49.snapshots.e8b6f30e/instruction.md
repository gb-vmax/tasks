# Bug Report

### Describe the bug

I'm experiencing an issue with the branch schema where the `snapshots` property is not returning an empty array as expected. After a recent update, the default snapshot generation logic seems to be causing problems when creating new branches.

### Reproduction

```js
const branch = {
  created: new Date(0),
  modified: new Date(0),
  name: 'my-branch'
};

// Apply branch schema defaults
const snapshots = branchSchema.snapshots();

// Expected: []
// Actual: TypeError or unexpected behavior
```

The issue occurs when initializing a new branch object. The snapshots field should default to an empty array, but instead it's trying to access properties that don't exist on the context.

### Expected behavior

When creating a new branch without any existing snapshots, the `snapshots` property should default to an empty array `[]`. The schema should handle cases where `_snapshotCount` is undefined or not set.

### System Info
- Insomnia version: latest
- OS: All platforms

This is blocking branch creation in our workflow. Any help would be appreciated!

---
Repository: /testbed
