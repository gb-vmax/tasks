# Bug Report

### Describe the bug

The `md5Hash` function is now producing unexpected hash values that don't match the previous behavior. Hash values generated from the same input strings are completely different from what they were before, breaking compatibility with existing stored hashes.

### Reproduction

```js
import {md5Hash} from '@docusaurus/utils';

const input = '  test string  ';
const hash = md5Hash(input);

console.log(hash);
// Expected: hex-encoded MD5 hash of the full string including whitespace
// Actual: base64-encoded hash with whitespace trimmed
```

The hash output format has changed and whitespace is being stripped from the input before hashing, which causes:
1. Different hash values for strings with leading/trailing whitespace
2. Hash format changed from hex to base64 encoding

### Expected behavior

The `md5Hash` function should:
- Preserve the original input string without trimming whitespace
- Return hex-encoded hash values (not base64)

This is causing issues with content that relies on consistent hash generation, particularly for cache busting and file naming.

### System Info
- @docusaurus/utils version: latest
- Node version: 18.x

---
Repository: /testbed
