# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX vendor bundle where exported properties are not accessible correctly. It seems like only the first property from an export object is being defined, and all other exports are missing or inaccessible.

### Reproduction

```js
// When trying to import multiple exports from the MDX module
import { compile, compileSync, evaluate } from '@mdx-js/mdx'

// Only the first export works, others are undefined
console.log(typeof compile)      // Expected: 'function', Actual: depends on order
console.log(typeof compileSync)  // Expected: 'function', Actual: undefined
console.log(typeof evaluate)     // Expected: 'function', Actual: undefined
```

### Expected behavior

All exported functions and properties from the MDX module should be accessible and properly defined. Each named export should be available for use.

### System Info
- MDX version: 3.0.0
- Node version: Latest

This appears to have started happening recently. Previously all exports were working as expected.

---
Repository: /testbed
