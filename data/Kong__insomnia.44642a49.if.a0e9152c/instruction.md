# Bug Report

### Describe the bug

I'm experiencing an issue with environment variable validation in the editor. The validation for the reserved key `NUNJUCKS_TEMPLATE_GLOBAL_PROPERTY_NAME` seems to be inverted - it's allowing the reserved key at the root level where it should be blocked, and blocking it in nested objects where it should be allowed.

### Reproduction

When trying to use the reserved key name in environment variables:

1. At root level: The key is accepted without any validation error (but it should be rejected)
2. In nested objects: The key is rejected with a validation error (but it should be allowed)

Example scenario:
```js
// Root level - this gets accepted but shouldn't
{
  "_": "some value"  // No error thrown
}

// Nested level - this gets rejected but shouldn't  
{
  "parent": {
    "_": "some value"  // Error: "_ is a reserved key"
  }
}
```

### Expected behavior

The reserved key `NUNJUCKS_TEMPLATE_GLOBAL_PROPERTY_NAME` (typically `_`) should only be blocked at the root level of environment variables, not in nested objects. Nested objects should be able to use this key name freely.

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

---
Repository: /testbed
