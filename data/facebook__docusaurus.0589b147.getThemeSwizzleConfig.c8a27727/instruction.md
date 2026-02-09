# Bug Report

### Describe the bug

When trying to swizzle theme components, I'm getting an error instead of the expected fallback behavior. It seems like the swizzle command is crashing when a theme doesn't have a swizzle config defined.

### Reproduction

```bash
# Try to swizzle a component from a theme without swizzle config
npx docusaurus swizzle @docusaurus/theme-classic Footer
```

The command fails with an error instead of using the default/fallback configuration.

### Expected behavior

When a theme doesn't provide a swizzle configuration, the swizzle command should fall back to the default swizzle config and allow swizzling to proceed normally. The command shouldn't crash or throw errors in this case.

### System Info
- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
