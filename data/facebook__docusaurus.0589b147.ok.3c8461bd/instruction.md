# Bug Report

### Describe the bug

The `ok()` function is throwing an error when called with arguments, even though it should be validating them. This is breaking functionality that relies on assertion-style checks.

### Reproduction

```js
// This now throws an error unexpectedly
ok(true);  // Error: Unexpected arguments

// Even basic checks fail
ok(someCondition);  // Error: Unexpected arguments

// Only works without arguments
ok();  // Returns true
```

### Expected behavior

The `ok()` function should accept arguments for assertion/validation purposes without throwing errors. It should validate the truthiness of the provided value rather than rejecting any arguments.

### System Info
- Package: remark-mdx@3.0.0
- Node version: Latest

---
Repository: /testbed
