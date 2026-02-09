# Bug Report

### Describe the bug

The swizzle command is not respecting the `--wrap` flag anymore. When I try to wrap a component using `docusaurus swizzle --wrap`, it seems to ignore the flag and doesn't perform the wrap action as expected.

### Reproduction

```bash
npm run swizzle -- --wrap <theme-name> <component-name>
```

Or using the CLI directly:

```bash
docusaurus swizzle --wrap SomeTheme SomeComponent
```

### Expected behavior

When the `--wrap` flag is passed, the swizzle command should wrap the component, allowing me to customize it while keeping the original implementation. Instead, it appears to be doing something else or not recognizing the flag at all.

### System Info
- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

This was working fine in previous versions. Not sure what changed but the wrap functionality seems broken now.

---
Repository: /testbed
