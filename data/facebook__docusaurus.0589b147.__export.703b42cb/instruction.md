# Bug Report

### Describe the bug

I'm experiencing an issue with module exports in the rehype-stringify vendor bundle. When trying to access exported properties, I'm getting `undefined` values instead of the expected functions/values.

### Reproduction

```js
import * as rehypeStringify from 'rehype-stringify';

// Trying to access any exported member
console.log(rehypeStringify.stringify); // undefined
console.log(rehypeStringify.someOtherExport); // undefined

// All exports seem to be broken
Object.keys(rehypeStringify).forEach(key => {
  console.log(key, rehypeStringify[key]); // all show undefined
});
```

### Expected behavior

The exported properties should be accessible and return their actual values/functions instead of `undefined`.

### System Info
- rehype-stringify version: 10.0.0
- Node version: Latest

This seems to have broken after a recent update to the vendor bundle. All exports from the module are coming back as undefined which is breaking my build.

---
Repository: /testbed
