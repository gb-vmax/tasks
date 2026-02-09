# Bug Report

### Describe the bug

The `getName()` method in the request plugin context is returning unexpected results. It appears to be attempting some kind of variable interpolation and sanitization on request names, but these helper functions are defined outside of the returned object structure, causing a syntax error in the code.

### Reproduction

```js
// In a plugin, trying to access request name
const requestContext = context.request;
const name = requestContext.getName();
// This fails with a syntax error
```

The issue seems to be related to how the request name is being processed. Looking at the code structure, there are interpolation and sanitization functions that appear to be misplaced in the object definition.

### Expected behavior

The `getName()` method should return the request name without any syntax errors. The method should be properly defined within the object structure.

### System Info
- Insomnia version: latest
- Plugin context: request module

This is blocking plugin development as the request context API is broken. Any workaround would be appreciated!

---
Repository: /testbed
