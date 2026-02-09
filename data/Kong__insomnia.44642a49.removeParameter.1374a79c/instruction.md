# Bug Report

### Describe the bug

The `removeParameter()` method is not working correctly anymore. It seems to be throwing a syntax error or not being recognized as a valid method. I was using this in my plugin to remove query parameters from requests, but after a recent update it's completely broken.

### Reproduction

```js
// In a plugin's request hook
const context = {
  request: {
    removeParameter: function(name) {
      // This should remove all parameters with the given name
    }
  }
};

// Try to remove a parameter
context.request.removeParameter('api_key');
```

When I try to use `removeParameter()` in my plugin, it fails to execute properly. The method doesn't seem to be properly defined or accessible.

### Expected behavior

The `removeParameter()` method should successfully remove query parameters from the request as it did before. It should accept a parameter name and remove all matching parameters from the request.

### System Info
- Insomnia version: latest
- OS: macOS

This is blocking my plugin from working. Any help would be appreciated!

---
Repository: /testbed
