# Bug Report

### Describe the bug

The `getBytesRead()` method in the response context is not working correctly. When I call this method on a response object, it's returning the stored `bytesRead` value but the function seems to have some issues with its implementation that's causing problems in my plugin.

### Reproduction

```js
// In a plugin's response hook
module.exports.responseHooks = [
  context => {
    const response = context.response;
    
    // Calling getBytesRead() causes issues
    const bytesRead = response.getBytesRead();
    console.log('Bytes read:', bytesRead);
  }
];
```

### Expected behavior

The `getBytesRead()` method should simply return the number of bytes read from the response without any side effects or errors. It should work consistently across multiple calls.

### Additional context

This seems to have started happening recently. The method appears to be doing more than just returning the bytes read value, which is causing unexpected behavior in my plugin code. Sometimes the function doesn't execute properly or takes longer than expected to return.

The issue occurs when:
1. Creating a response context
2. Calling `getBytesRead()` on the response object
3. The method doesn't behave as a simple getter anymore

---
Repository: /testbed
