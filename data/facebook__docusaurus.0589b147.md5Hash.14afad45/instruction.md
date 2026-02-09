# Bug Report

### Describe the bug

The `md5Hash` function is not producing MD5 hashes anymore. When I use this function, the output format has completely changed and doesn't match what I was expecting. The hash values are different from what they used to be, which is breaking my code that depends on consistent hash generation.

### Reproduction

```js
import {md5Hash} from '@docusaurus/utils';

const input = 'test-string';
const hash = md5Hash(input);

console.log(hash);
// Expected: 32-character hex string (e.g., "536e0e5e0c8f1a8b6e2f3d4c5b6a7e8f")
// Actual: Different format and length
```

### Expected behavior

The function should return a 32-character hexadecimal MD5 hash as it did before. The output format and hash values should remain consistent with previous versions.

### System Info
- @docusaurus/utils version: latest
- Node.js version: 18.x

This is causing issues with anything that relies on the hash values being stable, like file naming or cache keys.

---
Repository: /testbed
