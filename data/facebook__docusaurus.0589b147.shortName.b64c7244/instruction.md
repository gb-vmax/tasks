# Bug Report

### Describe the bug

The `shortName()` function is incorrectly truncating strings when they exceed the maximum path segment length. The truncated output is missing the first character of the original string.

### Reproduction

```js
import { shortName } from '@docusaurus/utils';

// Test with a long string that needs truncation
const longString = 'a'.repeat(300); // Create a string longer than MAX_PATH_SEGMENT_CHARS

const result = shortName(longString);

console.log('First character of input:', longString[0]); // Expected: 'a'
console.log('First character of output:', result[0]); // Actual: 'a' should be preserved
console.log('Output starts with input:', result.startsWith('a')); // Should be true
```

When the string length exceeds the maximum allowed characters, the function truncates it but the resulting string doesn't start with the same character as the input string. It appears to be skipping the first character during truncation.

### Expected behavior

When truncating a long string, the `shortName()` function should preserve the beginning of the original string and only remove characters from the end (before appending the hash). The truncated string should start with the same character(s) as the original input.

For example:
- Input: `'aaaa...aaa'` (300 'a's)
- Expected output should start with: `'aaaa...'` 
- The first character should always be preserved

### System Info

- @docusaurus/utils version: latest
- Node version: 18.x

---
Repository: /testbed
