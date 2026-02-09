# Bug Report

### Describe the bug

Environment variable keys that start with `$` or contain `.` are being accepted when they should be rejected. The validation seems to be inverted - keys that should fail validation are passing, and the error message shown doesn't match the actual validation rule.

### Reproduction

```js
// These keys should be invalid but are currently accepted:
const key1 = "$myVariable";
const key2 = "my.variable";

// When creating environment variables with these keys, 
// no validation error is shown even though they violate NeDB key constraints
```

### Expected behavior

Keys starting with `$` or containing `.` should be rejected with an appropriate error message explaining that these characters are not allowed. Currently, valid keys are being incorrectly flagged instead.

### Additional context

This appears to affect environment variable creation in the editor. The validation logic seems backwards - it's returning an error for valid keys instead of invalid ones.

---
Repository: /testbed
