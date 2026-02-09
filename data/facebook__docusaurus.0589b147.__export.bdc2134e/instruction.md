# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with module exports not being accessible. Properties that should be exported from modules are returning `undefined` when trying to access them.

### Reproduction

```js
// Trying to access exported properties
import { someFunction } from 'remark-rehype';

console.log(someFunction); // undefined
```

The exported functions/properties appear to be defined in the module but can't be read. This is breaking my build process.

### Expected behavior

Exported properties should be readable and accessible when imported from the module. The getter should work correctly to retrieve the exported values.

### System Info
- remark-rehype version: 11.0.0
- Node version: Latest
- Build tool: Jest/bundler

---
Repository: /testbed
