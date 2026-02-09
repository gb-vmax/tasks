# Bug Report

### Describe the bug

When using the swizzle command, the option normalization seems to be setting incorrect default values. Specifically, when I explicitly set `--typescript=false`, it still gets enabled if `--javascript` is passed. Similarly, when I set `--eject=false`, it gets overridden if `--wrap` is provided.

### Reproduction

```bash
# Case 1: typescript gets enabled even when explicitly disabled
docusaurus swizzle --typescript=false --javascript

# Case 2: eject gets enabled even when explicitly disabled  
docusaurus swizzle --eject=false --wrap
```

### Expected behavior

When a user explicitly sets an option to `false`, it should remain `false` regardless of other options being passed. The default value fallback should only apply when the option is `undefined`, not when it's explicitly set to `false`.

For example:
- `--typescript=false --javascript` should result in `typescript: false`
- `--eject=false --wrap` should result in `eject: false`

### System Info
- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

This is causing issues in our CI pipeline where we need to explicitly disable certain options but they're being overridden by the presence of other flags.

---
Repository: /testbed
