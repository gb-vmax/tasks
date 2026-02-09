# Bug Report

### Describe the bug

After a recent update, the swizzle command is not correctly mapping plugin configurations to their corresponding plugin instances. When running swizzle, I'm getting the wrong plugin config matched with each plugin, which causes the swizzle operation to fail or target the wrong component.

### Reproduction

```bash
# Setup a Docusaurus site with multiple plugins
npx docusaurus swizzle <plugin-name> <component-name>
```

The command either:
- Fails to find the correct plugin configuration
- Attempts to swizzle from the wrong plugin
- Shows incorrect plugin information in the swizzle UI

### Expected behavior

The swizzle command should correctly match each plugin instance with its corresponding configuration from the site config. Each plugin should be able to swizzle its own components without mixing up configurations between different plugins.

### System Info
- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

This seems to have started happening recently. The plugin-to-config mapping appears to be off by one or something similar.

---
Repository: /testbed
