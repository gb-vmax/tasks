# Bug Report

### Describe the bug

When trying to swizzle components from a specific theme plugin, the swizzle command is using the wrong plugin configuration. Instead of getting the config from the selected theme, it appears to always use the first plugin in the array, which causes swizzling to fail or use incorrect component definitions.

### Reproduction

```js
// Setup with multiple theme plugins
const plugins = [
  { name: '@docusaurus/theme-classic', ... },
  { name: '@docusaurus/theme-custom', ... }
]

// Try to swizzle from the custom theme
docusaurus swizzle @docusaurus/theme-custom ComponentName
```

The command doesn't respect the specified theme name and seems to pull configuration from the wrong plugin.

### Expected behavior

The swizzle command should use the configuration from the theme plugin that matches the provided `themeName`, not always default to the first plugin in the plugins array.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
