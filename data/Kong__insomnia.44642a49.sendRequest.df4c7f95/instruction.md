# Bug Report

### Describe the bug
After a recent update, network requests through the plugin API are failing with incomplete/truncated code. When trying to send requests using `context.network.sendRequest()`, the function appears to be cut off and doesn't complete properly, resulting in syntax errors.

### Reproduction
```js
// In a plugin
module.exports.requestHooks = [
  context => {
    context.network.sendRequest(context.request)
      .then(response => {
        console.log('Response:', response);
      });
  }
];
```

When executing this code, the request fails to complete and the plugin crashes with a syntax error.

### Expected behavior
The `sendRequest` function should complete successfully and return a response object as it did in previous versions. The function should properly handle the request lifecycle including rendering, transformation, sending, and response creation.

### Additional context
This seems to have broken after changes to the network context implementation. The code appears to be incomplete - it looks like the function definition was modified but not fully implemented. The response transformation and model creation steps seem to be missing.

### System Info
- Insomnia version: latest
- OS: Multiple platforms affected

---
Repository: /testbed
