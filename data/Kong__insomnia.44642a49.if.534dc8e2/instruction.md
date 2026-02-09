# Bug Report

### Describe the bug

Environment variable keys that should be invalid are now being accepted, and valid keys are being rejected with an incorrect error message.

### Reproduction

When trying to use environment variables with certain keys:

```js
// This key should be rejected but is now accepted
const invalidKey = "$myVariable";  // starts with $
const anotherInvalidKey = "my.variable";  // contains a dot

// These valid keys are now incorrectly rejected
const validKey = "myVariable";
const anotherValidKey = "MY_VAR";
```

The validation logic seems to be inverted - keys that contain `$` or `.` are now allowed when they should be blocked, and normal keys are being rejected with the error message `"keyname" cannot contain a '.'` even when they don't contain a dot.

### Expected behavior

- Keys starting with `$` should be rejected with an appropriate error message
- Keys containing `.` should be rejected with an appropriate error message  
- Valid keys (alphanumeric, underscores, etc.) should be accepted without any errors

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
