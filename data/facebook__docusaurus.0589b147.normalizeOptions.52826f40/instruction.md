# Bug Report

### Describe the bug

When using the swizzle command with the `--wrap` or `--eject` flags, the behavior is reversed. Specifying `--wrap` performs an eject operation, and specifying `--eject` performs a wrap operation.

### Reproduction

```bash
# This command should wrap the component but instead ejects it
docusaurus swizzle @docusaurus/theme-classic Footer --wrap

# This command should eject the component but instead wraps it
docusaurus swizzle @docusaurus/theme-classic Footer --eject
```

### Expected behavior

- `--wrap` flag should create a wrapper component
- `--eject` flag should eject the original component

The flags are doing the opposite of what they're supposed to do.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
