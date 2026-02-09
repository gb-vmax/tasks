# Bug Report

### Describe the bug

After a recent update, the `getId()` method in the plugin request context is throwing errors when called without arguments. The method seems to expect parameters now but previously worked fine when called with no arguments.

### Reproduction

```js
// In a plugin's request context
const requestId = request.getId();
// Error: getId is not a function or behaves unexpectedly
```

The issue appears when:
1. Using the plugin API to access request information
2. Calling `request.getId()` without any parameters
3. The method either fails or returns unexpected results

### Expected behavior

`request.getId()` should return the request ID string without requiring any additional parameters, just like it did before. The API shouldn't break existing plugin code that relies on this method signature.

### Additional context

This is breaking existing plugins that depend on the request context API. The method signature seems to have changed but there's no documentation about what parameters it now expects or why the change was made.

---
Repository: /testbed
