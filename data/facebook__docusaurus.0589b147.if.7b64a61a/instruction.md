# Bug Report

### Describe the bug

The swizzle command is not working correctly when trying to eject components. It seems like the command is defaulting to "wrap" action even when the `--eject` flag is explicitly provided.

### Reproduction

```bash
npx docusaurus swizzle @docusaurus/theme-classic Footer --eject
```

Expected: Component should be ejected
Actual: Component is being wrapped instead of ejected

### Steps to reproduce

1. Run the swizzle command with the `--eject` flag
2. The component gets wrapped instead of ejected
3. This happens regardless of which component you're trying to swizzle

### Expected behavior

When using the `--eject` flag, the component should be ejected (fully copied to the src directory) rather than wrapped. The eject action should take precedence when explicitly specified.

### System Info

- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

This seems to have started happening recently. The wrap action appears to be taking priority over eject in some scenarios.

---
Repository: /testbed
