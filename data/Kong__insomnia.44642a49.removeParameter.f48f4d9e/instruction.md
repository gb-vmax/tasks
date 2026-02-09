# Bug Report

### Describe the bug

The `removeParameter` function in the request plugin context is not working correctly when trying to remove query parameters. It seems like the function signature has changed but I'm getting unexpected behavior when calling it.

### Reproduction

```js
// In a plugin script
const request = context.request;

// Add some parameters
request.setParameter('foo', 'bar');
request.setParameter('foo', 'baz');
request.setParameter('test', 'value');

// Try to remove a parameter
request.removeParameter('foo');
// Expected: removes the 'foo' parameter(s)
// Actual: getting errors or unexpected behavior
```

### Expected behavior

The `removeParameter` method should remove query parameters by name as it did before. If there are multiple parameters with the same name, it should remove all of them (or provide options to control this behavior).

### Additional context

This might be related to a recent change in how parameters are handled. The method used to work fine in previous versions but now seems to have issues with the parameter removal logic.

---
Repository: /testbed
