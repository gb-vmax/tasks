# Bug Report

### Describe the bug

Environment variable validation is broken - it's now rejecting valid keys and showing incorrect error messages. When trying to add environment variables, I'm getting the reserved key error message even for variables that should be allowed.

### Reproduction

Try adding any environment variable in a nested environment object (not at root level). For example:

```js
{
  "myEnv": {
    "apiKey": "test123"  // This gets rejected with reserved key error
  }
}
```

Also, trying to use the reserved property name `_` at the root level doesn't seem to be blocked anymore, which should not be allowed.

### Expected behavior

- Non-reserved keys should be accepted at any nesting level
- The `_` property name should only be blocked at the root level
- Error messages should only appear when actually trying to use a reserved key

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
