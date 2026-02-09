# Bug Report

### Describe the bug

The `docuHash` function is not correctly handling the root path `/`. When passing `/` as input, the function should return `'index'`, but it's currently generating a hash-based string instead.

### Reproduction

```js
import { docuHash } from '@docusaurus/utils';

// This should return 'index' but returns something else
const result = docuHash('/');
console.log(result); // Expected: 'index', Actual: '/-XXX' (where XXX is a hash)
```

### Expected behavior

When the input string is `/` (the root path), `docuHash` should return the string `'index'` to represent the index/home page. This is important for generating consistent and predictable filenames for the root route.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
