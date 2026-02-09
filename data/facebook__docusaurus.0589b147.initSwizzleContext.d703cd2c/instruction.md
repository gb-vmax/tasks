# Bug Report

### Describe the bug

I'm experiencing an issue with the swizzle command where it seems to be mapping plugins to the wrong configurations. When I try to swizzle a component, I get errors about mismatched plugin types or the wrong component being swizzled.

### Reproduction

```bash
# Try to swizzle a component from a specific plugin
npx docusaurus swizzle @docusaurus/theme-classic Footer
```

The command either fails with a configuration mismatch error or swizzles components from the wrong plugin entirely. It seems like there's an off-by-one issue where plugins are being paired with incorrect configurations.

### Expected behavior

The swizzle command should correctly match each plugin with its corresponding configuration and allow me to swizzle the intended component without errors.

### System Info
- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
