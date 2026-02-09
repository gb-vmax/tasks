# Bug Report

### Describe the bug

I'm experiencing an issue with the swizzle command where components that should be marked as safe for swizzling are being rejected, and vice versa. It seems like the safety check is inverted - components that are configured as safe are being treated as unsafe, and unsafe components are being allowed through.

### Reproduction

```bash
# Try to swizzle a component that's marked as safe in the theme config
npx docusaurus swizzle @docusaurus/theme-classic Footer --eject

# Expected: Should work without warnings since Footer is safe
# Actual: Getting warnings/errors about unsafe swizzling
```

Similarly, when trying to swizzle components that should require warnings:

```bash
# Try to swizzle a component that should show safety warnings
npx docusaurus swizzle @docusaurus/theme-classic SomeInternalComponent --eject

# Expected: Should show safety warnings
# Actual: No warnings shown, component is treated as safe
```

### Expected behavior

The swizzle command should respect the safety configuration defined in the theme. Components marked as `safe` should be swizzleable without warnings, while components marked as `unsafe` or `forbidden` should show appropriate warnings or be blocked.

### System Info

- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

This seems like it might be a regression as the swizzle safety checks were working correctly in previous versions.

---
Repository: /testbed
