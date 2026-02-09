# Bug Report

### Describe the bug

After a recent update, I'm getting a syntax error when trying to use the MDX library. The code fails to parse and throws an error about unexpected token. It seems like there's something wrong with the exports in the types module.

### Reproduction

```js
import { number } from '@mdx-js/mdx';

// This throws an error during module loading
console.log(number);
```

The error occurs immediately when trying to import anything from the package. Even basic imports that were working before are now broken.

### Expected behavior

The module should export the `number` utility correctly and allow it to be imported without syntax errors. This was working fine in previous versions.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
