# Bug Report

### Describe the bug

I'm encountering an issue with hash generation when using string inputs. The hashes being generated are inconsistent or incorrect, particularly when working with special characters or non-ASCII text.

### Reproduction

```js
import { hasherByType } from './utils/crypto';

const input = "test string with émojis 🎉";
const hash1 = hasherByType['xxhash64'](input);
const hash2 = hasherByType['xxhash64'](input);

// Hashes should be identical for the same input
console.log(hash1 === hash2); // Expected: true
```

When I hash the same string multiple times, I'm getting different results. This is breaking our caching mechanism that relies on consistent hash values.

### Expected behavior

Hashing the same string should always produce the same hash value. The encoding should be consistent across different environments (Node.js vs browser).

### System Info
- Node version: 18.x
- Browser: Chrome/Firefox

---
Repository: /testbed
