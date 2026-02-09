# Bug Report

### Describe the bug

Component names are not being sorted correctly in the swizzle command output. The sorting appears to be case-sensitive in an inconsistent way, causing components to be displayed in an unexpected order.

### Reproduction

When running the swizzle command with multiple components that have similar names but different casing, the output order is incorrect:

```
Expected order:
- Footer
- footer/Copyright
- footer/Layout

Actual order:
- Footer
- footer/Layout
- footer/copyright
```

The issue seems to affect components with path separators where the last segment should be compared case-insensitively, but currently only one side of the comparison is being lowercased.

### Expected behavior

Component names should be sorted alphabetically in a consistent, case-insensitive manner. When comparing path segments, both sides should use the same casing for comparison to ensure predictable ordering.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
