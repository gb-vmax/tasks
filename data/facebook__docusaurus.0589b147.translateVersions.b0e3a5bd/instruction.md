# Bug Report

### Describe the bug

When working with versioned documentation, I noticed that the first version in my version list is not appearing in the translated output. All other versions are being translated correctly, but the first one seems to be skipped entirely.

### Reproduction

Setup:
1. Configure multiple documentation versions (e.g., "current", "1.0", "0.9")
2. Add translation files for all versions
3. Build the site with translations enabled

Observed behavior:
- Only versions starting from the second one onwards are translated
- The first version in the list is completely missing from the output
- The last version appears to be duplicated in the translated results

Example configuration:
```js
versions: [
  { name: 'current', ... },
  { name: '1.0', ... },
  { name: '0.9', ... }
]
```

Expected: All three versions should be translated
Actual: Only '1.0' and '0.9' are processed, with '0.9' appearing twice

### Expected behavior

All versions in the versions array should be translated and included in the output, maintaining their original order without any duplicates.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
