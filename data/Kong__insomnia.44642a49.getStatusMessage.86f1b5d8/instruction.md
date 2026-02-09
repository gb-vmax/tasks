# Bug Report

### Describe the bug

The `getStatusMessage()` method in the response context is broken after a recent update. When calling this method from a plugin, I'm getting a syntax error and the plugin fails to execute.

### Reproduction

```js
// In a plugin response hook
module.exports.responseHooks = [
  context => {
    const statusMsg = context.response.getStatusMessage();
    console.log(statusMsg);
  }
];
```

When this code runs, it throws an error and the plugin doesn't work anymore.

### Expected behavior

The method should return the status message as a string (e.g., "OK", "Not Found", etc.) just like it did before. The plugin should execute without errors.

### Additional context

This was working fine in previous versions. It looks like something changed with how `getStatusMessage()` is defined in the response context, but I can't figure out what's wrong from the error alone.

---
Repository: /testbed
