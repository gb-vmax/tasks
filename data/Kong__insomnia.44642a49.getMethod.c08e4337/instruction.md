# Bug Report

### Describe the bug
After updating to the latest version, the plugin API's `request.getMethod()` is returning HTTP methods in uppercase format instead of preserving the original casing. This is breaking plugins that rely on the exact method string as stored.

### Reproduction
```js
// In a plugin's request hook
module.exports.requestHooks = [
  context => {
    const method = context.request.getMethod();
    console.log(method); // Now prints "GET" instead of "get"
    
    // This comparison now fails if the original method was lowercase
    if (method === 'get') {
      // This code path is no longer reached
    }
  }
];
```

### Expected behavior
`getMethod()` should return the HTTP method exactly as it was set/stored in the request, without any transformation. If the method was set as lowercase "get", it should return "get", not "GET".

### Additional context
This appears to have changed recently and is causing compatibility issues with existing plugins that expect the method string to match the stored value. Some APIs and testing scenarios specifically use lowercase method names.

---
Repository: /testbed
