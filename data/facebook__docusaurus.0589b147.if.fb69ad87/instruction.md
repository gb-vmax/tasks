# Bug Report

### Describe the bug

When using the swizzle command with the `--wrap` flag, the behavior seems to be inverted. Setting `--wrap` appears to result in a "nowrap" action, and the component wrapping functionality doesn't work as expected.

### Reproduction

```bash
# Trying to wrap a component
docusaurus swizzle @docusaurus/theme-classic Footer --wrap

# Expected: Component should be wrapped
# Actual: Component is not wrapped (nowrap behavior)
```

The issue appears to affect the swizzle command when explicitly using the `--wrap` option. The action that gets selected doesn't match what the flag indicates.

### Expected behavior

When passing `--wrap` to the swizzle command, the component should be wrapped. The flag value should directly correspond to the wrap action being selected.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
