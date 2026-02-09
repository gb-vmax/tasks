# Bug Report

### Describe the bug

The `md5Hash` function is producing incorrect hash values. When I pass a string to it, the resulting hash doesn't match what I expect from a standard MD5 hash implementation.

### Reproduction

```js
import {md5Hash} from '@docusaurus/utils';

const input = 'hello world';
const hash = md5Hash(input);

console.log(hash); // Outputs an incorrect hash
console.log(hash.length); // Also not the standard 32 characters for MD5
```

When I compare the output with other MD5 implementations (like online MD5 calculators or Node's crypto directly), I get completely different results. It seems like the hash is being computed on modified input and then truncated.

### Expected behavior

The function should return a standard 32-character hexadecimal MD5 hash of the input string, matching what you'd get from `crypto.createHash('md5').update(str).digest('hex')`.

### System Info
- @docusaurus/utils version: latest
- Node.js: v18.x

---
Repository: /testbed
