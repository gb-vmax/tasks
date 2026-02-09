# Bug Report

### Describe the bug

The swizzle command is behaving incorrectly when trying to list available components. When I run the command without the `--list` flag, it unexpectedly shows the component list and exits, but when I actually use the `--list` flag, it doesn't show anything and just proceeds to prompt for component selection.

### Reproduction

```bash
# This should prompt for component selection but instead lists components and exits
docusaurus swizzle @docusaurus/theme-classic

# This should list components but doesn't
docusaurus swizzle @docusaurus/theme-classic --list
```

### Expected behavior

- Running `docusaurus swizzle <theme>` should prompt for component selection
- Running `docusaurus swizzle <theme> --list` should display the list of available components and exit

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
