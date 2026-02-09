# Bug Report

### Describe the bug

The `shortName()` function is producing incorrect output when truncating long path segments. It appears to be cutting off characters incorrectly, resulting in malformed shortened names.

### Reproduction

```js
import { shortName } from '@docusaurus/utils';

// Test with a long string that needs truncation
const longName = 'a'.repeat(300);
const result = shortName(longName);

console.log('Expected: String should start with "a"');
console.log('Actual:', result[0]); // First character is missing or wrong
```

When the string length exceeds `MAX_PATH_SEGMENT_CHARS`, the truncation seems to be removing too many characters from the beginning or end. The shortened string doesn't match what we'd expect based on the max length constraints.

### Expected behavior

The `shortName()` function should:
1. Properly truncate strings that exceed the maximum path segment length
2. Preserve the beginning of the string when truncating
3. Return a valid shortened name that respects both character and byte length limits

### Additional context

This is affecting path generation in our documentation build, where long file names or slugs are being shortened incorrectly. The issue seems to affect both the character-based truncation and byte-based truncation code paths.

---
Repository: /testbed
