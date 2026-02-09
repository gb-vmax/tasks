# Bug Report

### Describe the bug

After a recent update, validation warnings are not being displayed correctly. Instead of showing the actual warning messages, I'm seeing `[object Object]` printed in the console.

### Reproduction

When validation warnings are triggered (for example, with invalid configuration), the output looks like:

```
[object Object]
[object Object]
```

Instead of the expected human-readable warning messages like:

```
"field" is required
"value" must be a string
```

### Expected behavior

Validation warnings should display the actual error messages in a readable format, not object references.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems to have started happening recently. The warnings are being logged but the messages themselves aren't being extracted properly.

---
Repository: /testbed
