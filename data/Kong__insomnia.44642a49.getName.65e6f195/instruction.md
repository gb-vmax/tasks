# Bug Report

### Describe the bug

The plugin context's `getName()` method is throwing syntax errors and causing the application to crash. It looks like there's a problem with the function definition - the code structure seems malformed.

### Reproduction

```js
// In a plugin, trying to access request name
const requestContext = context.request;
const name = requestContext.getName();
// Application crashes with syntax error
```

Steps to reproduce:
1. Create a plugin that uses the request context
2. Call `getName()` on the request context
3. Application fails to load/execute

### Expected behavior

The `getName()` method should return the request name without any syntax errors. It should work the same way it did before.

### Additional context

This appears to have started happening recently. The method was working fine previously and just returned the simple request name. Now the application won't even start up properly when plugins try to use this method.

---
Repository: /testbed
