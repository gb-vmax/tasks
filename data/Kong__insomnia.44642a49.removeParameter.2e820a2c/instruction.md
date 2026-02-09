# Bug Report

### Describe the bug

I'm experiencing an issue with the `removeParameter` method in the plugin context. When trying to remove a request parameter by name, the parameter is not being removed from the request. Instead, it seems like the opposite behavior is happening - all other parameters are being removed except the one I'm trying to delete.

### Reproduction

```js
// Given a request with multiple parameters
request.setParameter('foo', 'bar');
request.setParameter('baz', 'qux');
request.setParameter('test', 'value');

// Try to remove a specific parameter
request.removeParameter('foo');

// Expected: 'foo' parameter should be removed
// Actual: 'foo' parameter still exists, but 'baz' and 'test' are gone
```

### Expected behavior

When calling `removeParameter('foo')`, only the parameter named 'foo' should be removed from the request. All other parameters should remain intact.

### System Info
- Insomnia version: latest
- OS: macOS

This is blocking my workflow as I need to dynamically remove specific parameters from requests in my plugin scripts. Any help would be appreciated!

---
Repository: /testbed
