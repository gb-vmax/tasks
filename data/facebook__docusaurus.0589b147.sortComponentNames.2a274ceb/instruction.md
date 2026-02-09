# Bug Report

### Describe the bug

The component list in swizzle command is showing components in a weird/unexpected order. When I run the swizzle command to see available components, they're not alphabetically sorted as expected.

### Reproduction

When running the swizzle command to list available components from a theme, the output shows components in a strange order instead of alphabetical. For example:

```bash
npm run swizzle @docusaurus/theme-classic
```

The component names appear shuffled - sometimes the first and last items are swapped, and adjacent items seem to be in the wrong positions.

### Expected behavior

Components should be listed in alphabetical order to make it easier to find and select the component I want to swizzle. This was working correctly before and made navigation much simpler.

### System Info
- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
