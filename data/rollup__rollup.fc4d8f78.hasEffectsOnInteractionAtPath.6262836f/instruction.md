# Bug Report

### Describe the bug

I'm experiencing an issue with namespace variable side effect detection. When accessing properties on namespace imports, the tree-shaking behavior seems incorrect - it's not properly detecting when namespace member accesses have side effects.

### Reproduction

```js
import * as utils from './utils';

// Accessing a namespace member
const result = utils.someFunction;

// This should be analyzed for side effects but isn't being handled correctly
```

The problem appears when checking for side effects on namespace member accesses. The detection logic doesn't seem to work as expected when dealing with property access patterns on imported namespaces.

### Expected behavior

The bundler should correctly identify whether accessing properties on namespace imports has side effects, and tree-shake accordingly. Member variable lookups on namespaces should be properly analyzed to determine if they can be safely removed or if they need to be retained.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
