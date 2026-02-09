# Bug Report

### Describe the bug

When loading client modules from plugins, the system is returning `undefined` values in the array instead of properly flattening the results. This causes issues when plugins don't have client modules defined.

### Reproduction

```js
const plugins = [
  {
    path: '/path/to/plugin1',
    getClientModules: () => ['module1.js', 'module2.js']
  },
  {
    path: '/path/to/plugin2',
    // No getClientModules defined
  },
  {
    path: '/path/to/plugin3',
    getClientModules: () => ['module3.js']
  }
];

const result = loadClientModules(plugins);
// Result contains undefined values: ['/path/to/plugin1/module1.js', '/path/to/plugin1/module2.js', undefined, '/path/to/plugin3/module3.js']
```

### Expected behavior

The function should return a flat array of all client module paths, excluding any plugins that don't have client modules. Something like:
```js
['/path/to/plugin1/module1.js', '/path/to/plugin1/module2.js', '/path/to/plugin3/module3.js']
```

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
