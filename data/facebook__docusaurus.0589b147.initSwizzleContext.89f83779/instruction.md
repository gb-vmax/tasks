# Bug Report

### Describe the bug

When using the swizzle command, the plugin instance and plugin config are getting swapped in the swizzle context. This causes the swizzle command to fail or behave incorrectly when trying to access plugin properties.

### Reproduction

```bash
# Try to swizzle a component from a theme plugin
npx docusaurus swizzle @docusaurus/theme-classic Footer
```

The command fails or returns incorrect plugin information because the plugin instance and config objects are reversed in the context.

### Expected behavior

The swizzle command should correctly identify the plugin and its configuration, allowing components to be swizzled without errors. The `plugin` property should contain the plugin configuration and the `instance` property should contain the plugin instance.

### System Info
- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
