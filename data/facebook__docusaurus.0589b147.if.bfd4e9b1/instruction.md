# Bug Report

### Describe the bug

The swizzle command is incorrectly detecting the `--wrap` flag when it's not actually provided. When running swizzle without any action flags, it defaults to the wrap action instead of prompting the user to choose an action.

### Reproduction

```bash
# Running swizzle without --wrap flag
npx docusaurus swizzle @docusaurus/theme-classic Footer

# Expected: Should prompt for action (wrap or eject)
# Actual: Automatically uses wrap action without prompting
```

The issue seems to occur when the `wrap` option is present in the options object but set to a falsy value (like `false` or `undefined`). The command treats this as if `--wrap` was explicitly passed.

### Expected behavior

When neither `--wrap` nor `--eject` flags are provided, the CLI should prompt the user to select an action instead of defaulting to wrap.

### System Info
- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
