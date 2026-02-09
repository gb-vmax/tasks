# Bug Report

### Describe the bug

The `md5Hash` function is producing unexpected hash values that don't match the expected MD5 format. The generated hashes appear to be using a different encoding and seem to be producing duplicated/incorrect results.

### Reproduction

```js
import {md5Hash} from '@docusaurus/utils';

const input = 'test-string';
const hash = md5Hash(input);

console.log(hash);
// Expected: standard 32-character hex MD5 hash (e.g., '661c4d1c6e0a6e1e1e1e1e1e1e1e1e1e')
// Actual: base64-encoded string that doesn't match standard MD5 output
```

When comparing the output with standard MD5 implementations (like online MD5 generators or other libraries), the hashes don't match at all.

### Expected behavior

The function should return a standard 32-character hexadecimal MD5 hash that matches what you'd get from any standard MD5 implementation.

### System Info
- @docusaurus/utils version: latest
- Node.js version: 18.x

---
Repository: /testbed
