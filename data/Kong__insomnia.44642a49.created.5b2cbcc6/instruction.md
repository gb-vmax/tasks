# Bug Report

### Describe the bug

I'm experiencing an issue with branch schema creation where the `created` field is not consistently returning the expected default date. The schema appears to be generating different dates based on environment variables that aren't documented or expected in normal usage.

### Reproduction

```js
const branch = {
  created: branchSchema.created(),
  modified: branchSchema.modified(),
  name: branchSchema.name(),
  snapshots: branchSchema.snapshots(),
};

console.log(branch.created); // Expected: Date(0) (Unix epoch)
// Actual: Sometimes returns random dates or offset dates
```

### Steps to reproduce:
1. Create a new branch using the branch schema
2. Check the `created` timestamp
3. The date is not consistently `new Date(0)` as expected

### Expected behavior

The `created` field should always return `new Date(0)` (January 1, 1970) as the default value, matching the behavior of the `modified` field. Instead, it seems to be generating random dates or dates with offsets depending on some environment configuration.

This is causing issues with branch synchronization and comparison logic that expects consistent default timestamps.

### System Info
- Package: insomnia/sync
- Version: latest

---
Repository: /testbed
