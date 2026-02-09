# Bug Report

### Describe the bug

After a recent update, the plugin network context seems to have broken syntax. When trying to use the `sendRequest` method in a plugin, I'm getting syntax errors and the request doesn't execute at all.

### Reproduction

```js
const response = await context.network.sendRequest(request);
```

This code that previously worked now fails completely. The plugin system appears to have a malformed function definition that's preventing any network requests from being sent through the plugin API.

### Expected behavior

The `sendRequest` method should execute successfully and return a response object as it did before. Plugins should be able to make HTTP requests without encountering syntax errors.

### System Info
- Insomnia version: latest
- OS: macOS

### Additional context

This is blocking my plugin from functioning at all. It looks like there might be incomplete code in the network context module - the function definition seems malformed or cut off.

---
Repository: /testbed
