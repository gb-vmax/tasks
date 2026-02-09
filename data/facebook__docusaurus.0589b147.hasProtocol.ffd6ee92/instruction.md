# Bug Report

### Describe the bug

The `hasProtocol` function is not correctly detecting URLs with protocols. It seems to be treating some URLs as having a protocol when they shouldn't be, or vice versa.

### Reproduction

```js
import { hasProtocol } from '@docusaurus/client';

// These should return true (URLs with protocols)
console.log(hasProtocol('http://example.com')); // expected: true
console.log(hasProtocol('https://example.com')); // expected: true
console.log(hasProtocol('mailto:test@example.com')); // expected: true

// These should return false (URLs without protocols)
console.log(hasProtocol('//example.com')); // expected: false
console.log(hasProtocol('/docs/intro')); // expected: false
console.log(hasProtocol('./relative/path')); // expected: false
```

The function appears to be incorrectly identifying protocol-relative URLs (starting with `//`) and possibly other edge cases.

### Expected behavior

The `hasProtocol` function should accurately determine whether a URL string contains a protocol scheme (like `http:`, `https:`, `mailto:`, etc.) and return `true` only for those cases. Protocol-relative URLs starting with `//` should return `false` since they don't have an explicit protocol.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
