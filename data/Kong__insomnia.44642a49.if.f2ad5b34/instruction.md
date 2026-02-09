# Bug Report

### Describe the bug

I'm experiencing an issue with environment variable validation in the editor. The reserved key `"_"` (underscore) is being incorrectly validated - it's now allowed at the root level when it should be restricted, but it's being blocked in nested objects when it should be allowed there.

### Reproduction

```js
// This should be blocked but is currently allowed:
const rootEnv = {
  "_": "some value"  // Should show error: "_" is a reserved key
}

// This should be allowed but is currently blocked:
const nestedEnv = {
  myObject: {
    "_": "some value"  // Should be valid but shows error
  }
}
```

### Expected behavior

The `"_"` key should only be reserved at the root level of environment objects. Nested objects should be able to use `"_"` as a property name without validation errors.

### System Info
- Insomnia version: latest
- OS: Multiple platforms affected

---
Repository: /testbed
