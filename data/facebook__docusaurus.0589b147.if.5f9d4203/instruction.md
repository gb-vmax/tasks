# Bug Report

### Describe the bug

The validation warning messages are not being displayed correctly. When validation errors occur, I'm getting `undefined` values in the warning output instead of the actual error messages.

### Reproduction

When I trigger a validation error in my Docusaurus config, the console output shows something like:

```
[WARNING] undefined, undefined
```

instead of the actual validation error messages that should explain what's wrong.

### Expected behavior

The warning should display the actual validation error messages, like:

```
[WARNING] "title" is required
[WARNING] "url" must be a valid URL
```

This makes it really hard to debug configuration issues since I can't see what's actually wrong.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
