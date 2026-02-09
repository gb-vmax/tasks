# Bug Report

### Describe the bug

The swizzle command is exiting unexpectedly when a theme name is provided. When trying to swizzle a component from a specific theme, the command just lists available themes and exits instead of proceeding with the swizzle operation.

### Reproduction

```bash
npx docusaurus swizzle @docusaurus/theme-classic Footer
```

Expected: The command should proceed to swizzle the Footer component
Actual: The command lists available themes and exits with code 1

This also happens with any theme name:
```bash
npx docusaurus swizzle my-custom-theme SomeComponent
```

### Expected behavior

When a theme name is provided as a parameter, the swizzle command should validate the theme name and proceed with the swizzle operation, not just list available themes and exit.

The `--list` flag should be the only way to trigger the theme listing behavior.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
