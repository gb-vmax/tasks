# Bug Report

### Describe the bug

The `isValidUrl()` function is incorrectly validating URLs. It's returning `true` for invalid URL strings that should fail validation.

### Reproduction

```js
import { isValidUrl } from './utils/url'

// These should return false but are returning true
console.log(isValidUrl('not a url'))  // returns true (expected: false)
console.log(isValidUrl(''))  // returns true (expected: false)
console.log(isValidUrl('invalid://'))  // returns true (expected: false)

// Valid URLs still work correctly
console.log(isValidUrl('https://example.com'))  // returns true (correct)
```

### Expected behavior

The function should return `false` for malformed or invalid URL strings, and only return `true` for properly formatted URLs.

### Additional context

This seems to have broken recently - the function was working correctly before. Now it's accepting strings that clearly aren't valid URLs.

---
Repository: /testbed
