# Bug Report

### Describe the bug

I'm encountering an issue with the swizzle command where it's not finding the swizzle configuration correctly. When trying to swizzle components, the command seems to be looking in the wrong place for the `getSwizzleConfig` function, which results in components not being properly configured.

### Reproduction

1. Create a plugin with a `getSwizzleConfig` export in the plugin module
2. Try to swizzle a component from that plugin using the CLI
3. The swizzle config is not properly loaded

The issue appears to be related to how the swizzle system accesses the plugin's configuration. It's trying to access properties that don't exist in the expected structure.

### Expected behavior

The swizzle command should correctly locate and use the `getSwizzleConfig` function from the plugin module, allowing components to be swizzled with their proper configurations (safe/unsafe actions, descriptions, etc.).

Additionally, when using the fallback `getSwizzleComponentList`, all expected actions (both `eject` and `wrap`) should be available as safe actions by default.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
