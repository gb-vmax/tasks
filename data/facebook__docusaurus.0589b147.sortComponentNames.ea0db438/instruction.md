# Bug Report

### Describe the bug

The component name sorting in the swizzle command is producing incorrect results. When listing available components to swizzle, the order appears wrong - components are not properly sorted alphabetically.

### Reproduction

When running the swizzle command to list available components, the output shows components in an unexpected order:

```bash
npm run swizzle @docusaurus/theme-classic
```

Expected output (alphabetically sorted):
```
- ComponentA
- ComponentB  
- componentC
- ComponentD
```

Actual output:
```
- ComponentA
- ComponentD
- ComponentB
- componentC
```

The sorting seems to be case-sensitive or using an incorrect comparison, causing lowercase component names to appear out of order relative to uppercase ones.

### Expected behavior

Component names should be sorted alphabetically in a case-insensitive manner, so that all components appear in proper alphabetical order regardless of casing.

### System Info
- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
