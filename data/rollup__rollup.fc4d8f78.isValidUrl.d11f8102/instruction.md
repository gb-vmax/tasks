# Bug Report

### Describe the bug
The `isValidUrl()` function is returning `true` for all inputs, even when they're invalid URLs. It seems like the validation logic isn't working properly anymore.

### Reproduction
```js
import { isValidUrl } from './utils/url'

console.log(isValidUrl('https://example.com'))  // Expected: true, Actual: true ✓
console.log(isValidUrl('not a url'))            // Expected: false, Actual: true ✗
console.log(isValidUrl(''))                     // Expected: false, Actual: true ✗
console.log(isValidUrl('javascript:alert(1)'))  // Expected: false, Actual: true ✗
```

### Expected behavior
The function should return `false` for invalid URLs and only return `true` for properly formatted URLs.

### System Info
- Node version: 18.x
- TypeScript version: 5.x

---
Repository: /testbed
