# Bug Report

### Describe the bug

I'm experiencing an issue with external module chunks where the `moduleInfo` property appears to be returning the wrong data. Instead of getting the expected module information object, I'm getting what looks like output options data.

### Reproduction

```js
import ExternalChunk from './ExternalChunk';

const externalModule = {
  id: 'my-external-module',
  info: {
    id: 'my-external-module',
    isExternal: true,
    // ... other module info properties
  },
  renormalizeRenderPath: false,
  suggestedVariableName: 'myModule'
};

const outputOptions = {
  format: 'es',
  // ... other output options
};

const chunk = new ExternalChunk(externalModule, outputOptions, '/base/path');

// Expected: module.info object
// Actual: outputOptions object
console.log(chunk.moduleInfo);
```

### Expected behavior

The `moduleInfo` property should contain the module's info object (with properties like `id`, `isExternal`, etc.), not the output options configuration.

### System Info
- Rollup version: latest
- Node version: 18.x

This is causing issues when trying to access module metadata from external chunks. Any help would be appreciated!

---
Repository: /testbed
