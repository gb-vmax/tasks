# Bug Report

### Describe the bug

The `removeParameter()` method in the plugin request context has changed its behavior and now returns a boolean value. This breaks existing plugins that don't expect a return value from this method.

### Reproduction

```js
// In a plugin that uses the request context
module.exports.requestHooks = [
  context => {
    // This used to work fine, but now removeParameter returns a boolean
    context.request.removeParameter('api_key');
    
    // If code was checking the result like this, it will break:
    const result = context.request.removeParameter('token');
    // result is now a boolean instead of undefined
  }
];
```

### Expected behavior

The `removeParameter()` method should maintain backward compatibility and not return a value (or at least document this breaking change). Existing plugins that may be using this method should continue to work without modification.

### Additional context

This appears to have been introduced recently. The method previously had no return value, but now returns a boolean indicating whether parameters were removed. While this might be useful information, it's a breaking change for the API.

---
Repository: /testbed
