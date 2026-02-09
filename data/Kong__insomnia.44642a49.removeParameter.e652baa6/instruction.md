# Bug Report

### Describe the bug
The `removeParameter()` method in the plugin context API is not removing parameters correctly. When I try to remove a query parameter from a request, it's still present in the request instead of being removed.

### Reproduction
```js
// In a plugin
const context = {
  request: {
    // ... other methods
    removeParameter: function(name) {
      // Call this to remove a parameter
    }
  }
}

// Try to remove a parameter named 'api_key'
context.request.removeParameter('api_key')

// Expected: parameter should be gone
// Actual: parameter is still there
```

### Steps to reproduce
1. Create a request with query parameters
2. Use the plugin API to call `removeParameter()` with a parameter name
3. Check if the parameter was removed from the request
4. The parameter remains in the request

### Expected behavior
When calling `removeParameter(name)`, the specified parameter should be removed from the request's parameters array. The parameter should no longer be included in the request.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
