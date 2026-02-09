# Bug Report

### Describe the bug

Client module paths are being resolved incorrectly, resulting in broken module imports. When plugins define client modules, the paths are not being constructed properly, which causes the application to fail loading these modules.

### Reproduction

```js
// In a plugin configuration
module.exports = function (context, options) {
  return {
    name: 'my-plugin',
    getClientModules() {
      return ['./src/clientModule.js'];
    },
  };
};
```

When the plugin tries to load the client module, the path resolution fails because the module path and plugin path are being combined in the wrong order.

### Expected behavior

Client modules should be loaded successfully with their paths resolved relative to the plugin's directory. The resolved path should be `<plugin-path>/src/clientModule.js`, but instead it's trying to resolve as `<client-module-path>/<plugin-path>`.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
