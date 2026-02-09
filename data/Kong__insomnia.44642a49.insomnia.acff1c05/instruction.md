# Bug Report

### Describe the bug

I'm encountering a syntax error when trying to use the plugin export API. It seems like there's a problem with the `data.export.insomnia` method definition - the code won't even parse/load properly.

### Reproduction

```js
const context = require('insomnia-plugin-context');

// Attempting to call the export method
await context.data.export.insomnia({
  includePrivate: true,
  format: 'json'
});
```

When I try to use this, I get a syntax error and the plugin fails to load. The error appears to be related to how the export object is structured.

### Expected behavior

The `data.export.insomnia` method should be callable and properly export workspace data as it did before. The method should accept the options object and return the exported data without any parsing issues.

### System Info
- Insomnia version: latest
- OS: macOS

This seems to have started happening recently. The export functionality was working fine in the previous version.

---
Repository: /testbed
