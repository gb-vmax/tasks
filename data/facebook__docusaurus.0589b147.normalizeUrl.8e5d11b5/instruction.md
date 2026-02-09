# Bug Report

### Describe the bug

The `normalizeUrl` function is not handling URL normalization correctly when the first URL segment is a protocol. After recent changes, URLs with protocols are being processed incorrectly, causing the protocol portion to be included in the slash normalization logic.

### Reproduction

```js
import {normalizeUrl} from '@docusaurus/utils';

// Protocol URLs are broken
const result1 = normalizeUrl(['https:', 'example.com', 'path']);
console.log(result1);
// Expected: https://example.com/path
// Actual: Incorrect output with malformed protocol handling

const result2 = normalizeUrl(['http:', 'localhost:3000', 'docs']);
console.log(result2);
// Expected: http://localhost:3000/docs
// Actual: Incorrect output

const result3 = normalizeUrl(['file:', '/absolute/path']);
console.log(result3);
// Expected: file:///absolute/path
// Actual: Incorrect output
```

The issue appears when combining protocol strings with subsequent path segments. The function is now processing the protocol part through the slash removal logic when it shouldn't be.

### Expected behavior

URLs with protocol prefixes should be properly combined with their path components, maintaining the correct number of slashes after the protocol (e.g., `https://` or `file:///`).

### System Info

- @docusaurus/utils version: latest
- Node version: 18.x

---
Repository: /testbed
