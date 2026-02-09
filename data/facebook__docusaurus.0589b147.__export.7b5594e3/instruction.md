# Bug Report

### Describe the bug

I'm experiencing an issue with module exports in the remark-gfm vendor bundle. When trying to use exported functions or properties from the module, I'm getting `undefined` values or the exports aren't being properly exposed.

### Reproduction

```js
// Attempting to import from remark-gfm
import { someFunction } from 'remark-gfm';

// someFunction is undefined
console.log(someFunction); // undefined

// Or when accessing exported properties directly
const remarkGfm = require('remark-gfm');
console.log(remarkGfm.exports); // properties are missing or undefined
```

### Expected behavior

All exported functions and properties from the remark-gfm module should be accessible and properly defined when imported or required.

### System Info
- Version: 4.0.0
- Node version: Latest

This seems to have broken after a recent update to the vendor bundle. The module loads without errors but the actual exports aren't available for use.

---
Repository: /testbed
