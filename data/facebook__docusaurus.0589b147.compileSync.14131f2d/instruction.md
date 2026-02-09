# Bug Report

### Describe the bug

After a recent update, the `compileSync` function from `@mdx-js/mdx` is not working properly. The exported function appears to be broken or incorrectly defined, causing syntax errors when trying to use it.

### Reproduction

```js
import { compileSync } from '@mdx-js/mdx';

const result = compileSync('# Hello World');
console.log(result);
```

When running this code, I get syntax errors indicating that `compileSync` is not properly exported or defined. It seems like the export statement got corrupted somehow.

### Expected behavior

The `compileSync` function should be properly exported and callable. It should compile MDX content synchronously and return the compiled result without throwing syntax errors.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This was working fine before, not sure what changed but the export seems malformed now.

---
Repository: /testbed
