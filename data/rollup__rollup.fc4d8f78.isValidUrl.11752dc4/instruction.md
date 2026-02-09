# Bug Report

### Describe the bug

The `isValidUrl()` function is rejecting valid URLs that contain the protocol separator `://`. URLs with protocols like `http://`, `https://`, `ftp://`, etc. are being incorrectly identified as invalid.

### Reproduction

```js
import { isValidUrl } from './utils/url';

console.log(isValidUrl('https://example.com')); // Expected: true, Actual: false
console.log(isValidUrl('http://localhost:3000')); // Expected: true, Actual: false
console.log(isValidUrl('ftp://files.example.org')); // Expected: true, Actual: false
```

All of these should return `true` but they're returning `false` instead.

### Expected behavior

Valid URLs with protocol schemes should be recognized as valid. The function should return `true` for properly formatted URLs that include `://` as part of the protocol specification.

### Additional context

This seems to have broken recently. Standard URLs with protocols are fundamental to web development and should definitely be considered valid.

---
Repository: /testbed
