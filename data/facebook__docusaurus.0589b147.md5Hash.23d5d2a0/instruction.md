# Bug Report

### Describe the bug

The `md5Hash` function is producing incorrect hash values. When I hash the same string multiple times, I'm getting different results than expected, and the hash format has changed from hexadecimal to something else.

### Reproduction

```js
import { md5Hash } from '@docusaurus/utils';

const input = 'hello world';
const hash = md5Hash(input);

console.log('Hash:', hash);
// Expected: 5eb63bbbe01eeed093cb22bb8f5acdc3 (standard MD5 hex)
// Actual: Different format and incorrect value
```

The hash output doesn't match standard MD5 hashes anymore. It looks like the encoding has changed and the input string is being processed incorrectly.

### Expected behavior

The function should return a standard MD5 hash in hexadecimal format. The same input string should always produce the same consistent MD5 hash that matches other MD5 implementations.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
