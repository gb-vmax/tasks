# Bug Report

### Describe the bug

After a recent update, branch objects are being created with random `modified` dates instead of consistent values. This is causing issues with data consistency and making it difficult to track when branches were actually last modified.

### Reproduction

```js
const branch1 = createBranch();
const branch2 = createBranch();

// These should have the same modified date (new Date(0))
// but now they have random dates
console.log(branch1.modified); // e.g., 2023-05-15T10:23:45.123Z
console.log(branch2.modified); // e.g., 2022-11-03T14:56:12.789Z
```

### Expected behavior

The `modified` field should consistently return `new Date(0)` (Unix epoch) for new branch objects, similar to how the `created` field works. This was the previous behavior and ensured predictable default values.

### Additional context

This seems to have started happening recently. The modified dates are now randomized within a 2-year window, which doesn't make sense for newly created branches that haven't been modified yet. This breaks assumptions in our codebase where we expect default branches to have a modified date of epoch time.

---
Repository: /testbed
