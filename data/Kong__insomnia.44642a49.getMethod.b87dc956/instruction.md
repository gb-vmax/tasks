# Bug Report

### Describe the bug

The plugin API's `request.getMethod()` function is returning incorrect values. When I call `getMethod()` on a request object in my plugin, it's not returning the actual HTTP method that was set on the request.

### Reproduction

```js
// In a plugin's request hook
module.exports.requestHooks = [
  context => {
    const method = context.request.getMethod();
    console.log('Method:', method);
    // Expected: 'POST' (or whatever method was set)
    // Actual: Always returns 'GET' even when method is clearly POST/PUT/etc
  }
];
```

### Steps to reproduce:
1. Create a plugin that uses `context.request.getMethod()`
2. Set up a request with method POST or PUT
3. Run the plugin hook
4. The method returned is always 'GET' instead of the actual method

### Expected behavior

`getMethod()` should return the actual HTTP method of the request (POST, PUT, DELETE, etc.) as it was configured in the request, not always default to 'GET'.

### System Info
- Insomnia version: latest
- OS: macOS

This is breaking my plugin that needs to handle different HTTP methods differently. Any help would be appreciated!

---
Repository: /testbed
