# Bug Report

### Describe the bug

The plugin export API is not working correctly when trying to export workspaces. When calling `context.data.export.insomnia()`, I'm getting a syntax error or the export functionality is completely broken.

### Reproduction

```js
// In a plugin
module.exports.requestHooks = [
  context => {
    const exported = await context.data.export.insomnia({
      includePrivate: true,
      format: 'json'
    });
    console.log(exported);
  }
];
```

This throws an error and the export doesn't work at all. It was working fine before but seems to have broken recently.

### Expected behavior

The `context.data.export.insomnia()` method should successfully export workspace data in the specified format without throwing errors. The exported data should be returned as expected.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
