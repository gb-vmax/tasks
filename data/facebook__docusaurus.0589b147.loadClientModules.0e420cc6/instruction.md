# Bug Report

### Describe the bug

When loading client modules from plugins, the returned result has an unexpected nested array structure instead of a flat array of module paths. This causes issues when trying to process or import the client modules.

### Reproduction

```js
const plugins = [
  {
    path: '/path/to/plugin1',
    getClientModules: () => ['module1.js', 'module2.js']
  },
  {
    path: '/path/to/plugin2',
    getClientModules: () => ['module3.js']
  }
];

const modules = loadClientModules(plugins);
// Expected: ['/path/to/plugin1/module1.js', '/path/to/plugin1/module2.js', '/path/to/plugin2/module3.js']
// Actual: [['/path/to/plugin1/module1.js', '/path/to/plugin1/module2.js'], ['/path/to/plugin2/module3.js']]
```

### Expected behavior

`loadClientModules()` should return a flat array of absolute paths to all client modules across all plugins, not an array of arrays.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
