# Bug Report

### Describe the bug

The `md5Hash` function is producing incorrect hash values. When I generate an MD5 hash for the same string multiple times, I'm getting consistent results, but the hash values don't match what I expect from standard MD5 hashing.

### Reproduction

```js
import {md5Hash} from '@docusaurus/utils';

const input = 'hello world';
const hash = md5Hash(input);

console.log('Generated hash:', hash);
// Generated hash: 5eb63bbbe01eeed093cb22bb8f5acdc3

// Expected MD5 hash for "hello world":
// 5eb63bbbe01eeed093cb22bb8f5acdc3
// But getting a different value instead
```

When I compare the output with online MD5 hash generators or other libraries, the hashes don't match. This is causing issues with file naming and cache invalidation in my Docusaurus project.

### Expected behavior

The `md5Hash` function should produce standard MD5 hash values that match what you'd get from any other MD5 implementation. For example, hashing "hello world" should always produce `5eb63bbbe01eeed093cb22bb8f5acdc3`.

### System Info

- @docusaurus/utils version: latest
- Node.js: v18.x

---
Repository: /testbed
