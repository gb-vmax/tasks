# Bug Report

### Describe the bug

I'm experiencing an issue with generated class names when using Mantine components. It appears that certain special characters in the randomly generated class names are not being properly sanitized, which is causing CSS selector issues in my application.

### Reproduction

When Mantine components generate random class names internally, some special characters (specifically guillemet characters like `«` and `»`) are appearing in the output instead of being stripped out. This causes problems when these class names are used in CSS selectors or JavaScript DOM queries.

Example of problematic class name that might be generated:
```
__m__-:r1«2»3:
```

Expected class name format:
```
__m__-r123
```

### Expected behavior

All special characters that could cause issues in CSS selectors should be removed from the generated class names. The class names should only contain alphanumeric characters and safe separators like hyphens and underscores.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome/Firefox

---
Repository: /testbed
