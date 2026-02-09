# Bug Report

### Describe the bug

The code translation files are being written to the wrong directory path. Instead of being placed in the localization directory, they're being written to an incorrect nested path structure.

### Reproduction

When trying to use code translations with the i18n feature:

1. Set up a localization directory (e.g., `i18n/en`)
2. Try to generate or read code translation files
3. The files are created/looked up in the wrong location

For example, if the localization directory is `i18n/en`, the code translations file should be at:
```
i18n/en/code.json
```

But instead, it's being placed at:
```
i18n/code.json/en
```

This causes translation files to not be found or written to unexpected locations.

### Expected behavior

Code translation files should be written directly inside the localization directory path, not in a restructured parent/child directory arrangement.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
