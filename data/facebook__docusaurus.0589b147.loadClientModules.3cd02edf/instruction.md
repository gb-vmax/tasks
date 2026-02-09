# Bug Report

### Describe the bug

I'm experiencing an issue with client modules loading in Docusaurus. When a plugin doesn't have any client modules defined (when `getClientModules()` returns undefined or null), the build process seems to be including empty strings in the client modules array instead of just skipping those plugins entirely.

### Reproduction

```js
// Plugin without client modules
const plugin = {
  name: 'my-plugin',
  path: '/path/to/plugin',
  // No getClientModules defined
}

// The resulting client modules array contains empty strings
// Expected: []
// Actual: ['']
```

This happens when you have multiple plugins and some of them don't provide client modules. The array ends up with empty string entries which causes issues during the build.

### Expected behavior

Plugins without client modules should be filtered out completely, not result in empty string entries in the client modules array. The function should only return actual module paths.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
