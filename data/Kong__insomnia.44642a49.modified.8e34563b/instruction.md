# Bug Report

### Describe the bug

When creating branch objects, the `modified` field is being set to a random date instead of a consistent value. This causes issues when comparing branches or when tests expect deterministic behavior.

### Reproduction

```js
const branch1 = createBranch();
const branch2 = createBranch();

// These should be the same, but they're different
console.log(branch1.modified); // Some random date
console.log(branch2.modified); // Different random date
```

The problem seems to be that the `modified` field is now using `Math.random()` to generate timestamps, which means every branch created gets a different timestamp even when they should be identical.

### Expected behavior

Branch objects created without explicitly setting the `modified` field should have consistent, predictable timestamps (like `new Date(0)`). Random timestamps make it impossible to reliably compare branches or test branch-related functionality.

### Additional context

This appears to be related to some global configuration object (`__SCHEMA_DATE_CONFIG__`) that's being used to randomize timestamps. Not sure why this was added, but it's breaking the expected behavior where default schema values should be deterministic.

---
Repository: /testbed
