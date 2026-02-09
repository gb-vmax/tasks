# Bug Report

### Describe the bug
Environment variable keys that should be invalid are now being accepted, and valid keys are being rejected with an error message. The validation logic appears to be inverted.

### Reproduction
```js
// This should fail but doesn't
const result1 = ensureKeyIsValid('$invalid', false);
// Returns null (no error) when it should return an error

// This should pass but doesn't
const result2 = ensureKeyIsValid('validKey', false);
// Returns error message when it should return null
```

### Expected behavior
- Keys starting with `$` or containing `.` should be rejected with an error message
- Valid keys (without `$` at the start or `.` anywhere) should be accepted (return null)

Currently it's doing the opposite - rejecting valid keys and accepting invalid ones.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
