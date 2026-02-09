# Bug Report

### Describe the bug

I'm encountering an issue with environment variable key validation. When trying to create environment variables, valid keys are being incorrectly rejected as reserved, even when they're not the special `NUNJUCKS_TEMPLATE_GLOBAL_PROPERTY_NAME` key.

### Reproduction

```js
// Trying to add a regular environment variable in a nested scope
const key = "my_api_key";
const isRoot = false;

// This is incorrectly returning an error message
const error = ensureKeyIsValid(key, isRoot);
// Expected: null
// Actual: "_root is a reserved key"
```

Any environment variable key in a non-root context is being rejected with the reserved key error message, even though the key has nothing to do with the reserved property name.

### Expected behavior

Only the actual reserved key name (`_root` or whatever `NUNJUCKS_TEMPLATE_GLOBAL_PROPERTY_NAME` is set to) should be rejected when `isRoot` is true. Other keys should pass validation regardless of the `isRoot` parameter value.

### System Info
- Insomnia version: latest
- OS: macOS

This is blocking me from creating any environment variables in sub-environments. Any help would be appreciated!

---
Repository: /testbed
