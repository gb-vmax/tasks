# Bug Report

### Describe the bug

After a recent update, the application crashes with a syntax error when trying to execute requests with plugins enabled. The error appears to be related to malformed code in the HAR request processing logic.

### Reproduction

```js
// Any request that uses plugin hooks will fail
// For example:
1. Enable any plugin with request hooks
2. Try to send a request
3. Application crashes with syntax error
```

The issue occurs immediately when the plugin hook system tries to execute, preventing any requests from being sent when plugins are active.

### Expected behavior

Requests should execute normally with plugins enabled. The plugin hooks should be applied without syntax errors, and requests should complete successfully.

### System Info
- Insomnia version: latest
- OS: Any

### Additional context

This seems to have been introduced in a recent change to the plugin hook execution system. Disabling all plugins allows requests to work normally, but this breaks the plugin functionality entirely.

---
Repository: /testbed
