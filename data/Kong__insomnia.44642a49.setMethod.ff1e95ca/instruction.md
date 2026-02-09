# Bug Report

### Describe the bug

When using the plugin API to set HTTP methods on requests, the `setMethod()` function is not working as expected. After a recent update, calling `request.setMethod()` appears to have broken - methods are no longer being set on the request object properly.

### Reproduction

```js
// In a plugin's request context
const request = context.request;

// Try to set the method
request.setMethod('POST');

// The method doesn't get set correctly
console.log(request.getMethod()); // Expected: 'POST', but getting unexpected behavior
```

### Expected behavior

The `setMethod()` function should update the request's HTTP method. Previously this worked fine, but something seems to have changed recently that broke this functionality.

### Additional context

This is blocking our plugin from working correctly. We rely on being able to dynamically change request methods based on certain conditions. The issue appeared after the latest update.

---
Repository: /testbed
