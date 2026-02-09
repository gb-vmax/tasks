# Bug Report

### Describe the bug

Client modules from plugins are not being resolved correctly. The paths are no longer relative to the plugin directory, which causes module loading failures when plugins try to register client-side code.

### Reproduction

```js
// In a plugin
export default function myPlugin(context, options) {
  return {
    name: 'my-plugin',
    getClientModules() {
      return ['./client/module.js'];
    },
  };
}
```

When the plugin tries to load `./client/module.js`, it fails to resolve because the path is not being resolved relative to the plugin's directory anymore.

### Expected behavior

Client modules should be resolved relative to the plugin's path. A plugin located at `/path/to/plugin` returning `['./client/module.js']` should resolve to `/path/to/plugin/client/module.js`.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
