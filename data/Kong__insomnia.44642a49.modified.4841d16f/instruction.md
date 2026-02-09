# Bug Report

### Describe the bug
Branch objects are being created with an incorrect `modified` timestamp. Instead of being initialized to epoch (January 1, 1970), branches are now getting a timestamp 24 hours in the future from the current time.

### Reproduction
```js
// Create a new branch
const branch = createBranch();

// Check the modified timestamp
console.log(branch.modified);
// Expected: Thu Jan 01 1970 00:00:00 GMT+0000
// Actual: [tomorrow's date]
```

### Expected behavior
The `modified` field should be initialized to `new Date(0)` (epoch time) when a branch is first created, matching the behavior of the `created` field. This ensures consistency in the schema and prevents branches from appearing to have been modified before they were even created.

### Additional context
This affects branch synchronization logic and could cause issues with timestamp comparisons or sorting operations that rely on the modified date being set to epoch initially.

---
Repository: /testbed
