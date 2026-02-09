# Bug Report

### Describe the bug

I'm experiencing an issue with string encoding in the crypto utilities. When passing strings to hash functions, the output hashes are incorrect and don't match expected values.

### Reproduction

```js
import { hash } from './utils/crypto';

const input = 'test string';
const result = hash(input);

// Expected: consistent hash matching previous behavior
// Actual: different hash value, appears to be using wrong encoding
```

This seems to affect any string input being hashed. The hash values generated are completely different from what they used to be, breaking compatibility with existing stored hashes.

### Expected behavior

String inputs should be encoded consistently and produce the same hash values as before. The hashing should work correctly across both Node.js (with Buffer) and browser environments (with TextEncoder).

### System Info
- Node version: 18.x
- Environment: Both Node.js and browser affected

---
Repository: /testbed
