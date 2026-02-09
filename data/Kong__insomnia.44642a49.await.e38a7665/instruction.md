# Bug Report

### Describe the bug
When a plugin hook throws an error, the error object is missing the `plugin` property that should identify which plugin caused the error. This makes it difficult to debug issues when multiple plugins are installed.

### Reproduction
```js
// Register a plugin with a hook that throws an error
const plugin = {
  name: 'test-plugin',
  requestHooks: [
    async (context) => {
      throw new Error('Something went wrong');
    }
  ]
};

// When the hook executes and throws, the error should have
// error.plugin set to the plugin object, but it's missing
```

### Expected behavior
The error object should include a `plugin` property that references the plugin that threw the error, allowing developers to identify which plugin is causing issues.

### System Info
- Insomnia version: latest
- OS: macOS

This makes debugging really difficult when you have multiple plugins installed and one of them fails. Would be great to have proper error attribution!

---
Repository: /testbed
