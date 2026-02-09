# Bug Report

### Describe the bug

After updating to the latest version, the swizzle command is not correctly mapping plugins to their configurations. When trying to swizzle components from a plugin, I'm getting either the wrong plugin configuration or the command fails because it can't find the expected plugin.

### Reproduction

1. Set up a Docusaurus project with multiple plugins
2. Try to swizzle a component from a specific plugin using the CLI
3. The swizzle command either uses the wrong plugin configuration or skips the last plugin entirely

For example, if I have plugins A, B, and C installed and try to swizzle from plugin C, it doesn't work as expected. The plugin list seems to be misaligned with the actual plugin configurations.

### Expected behavior

The swizzle command should correctly match each plugin instance with its corresponding configuration, allowing me to swizzle components from any installed plugin regardless of its position in the plugin list.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
