# Bug Report

### Describe the bug
The `toBase64` function is producing incorrect output - the resulting base64 string appears to be reversed. When converting numbers to base64 encoding, the characters are appearing in the wrong order.

### Reproduction
```js
import { toBase64 } from './utils/base64';

// Converting a number to base64
const result = toBase64(123);
console.log(result);
// Output: reversed/incorrect base64 string
// Expected: correct base64 encoded value with proper character ordering
```

### Expected behavior
The function should return a properly formatted base64 string with characters in the correct order. The most significant digits should appear first, followed by less significant digits in the standard base64 encoding format.

### Additional context
This seems to have started happening recently. The base64 encoded strings are coming out backwards compared to what they should be.

---
Repository: /testbed
