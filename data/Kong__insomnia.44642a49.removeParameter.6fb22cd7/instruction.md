# Bug Report

### Describe the bug

After a recent update, the `removeParameter()` method in the plugin context is not working as expected. When I try to remove a parameter from a request, the parameter gets removed but the method also seems to be doing additional cleanup operations that are affecting other parameters.

### Reproduction

```js
const context = {
  request: {
    removeParameter: function(name) {
      // Call removeParameter on a request
    }
  }
}

// Try to remove a specific parameter
context.request.removeParameter('apiKey')

// Expected: Only 'apiKey' parameter should be removed
// Actual: Additional parameters are being filtered out unexpectedly
```

### Steps to reproduce:
1. Create a request with multiple parameters including some empty or disabled ones
2. Call `removeParameter()` with a specific parameter name
3. Check the remaining parameters

### Expected behavior

The method should only remove parameters matching the specified name. Other parameters, even if they're empty or disabled, should remain untouched unless explicitly removed.

### Additional context

This appears to have started happening recently. The method seems to be doing some extra cleanup of parameters that have empty names/values, which wasn't the case before. This is causing issues in my plugin where I need to preserve certain empty parameters for later use.

---
Repository: /testbed
