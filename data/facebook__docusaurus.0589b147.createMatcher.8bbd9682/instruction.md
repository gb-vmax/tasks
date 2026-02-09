# Bug Report

### Describe the bug

I'm experiencing unexpected behavior with the glob pattern matching functionality. When I pass an empty array of patterns to `createMatcher`, it's matching everything instead of matching nothing.

### Reproduction

```js
import { createMatcher } from '@docusaurus/utils';

// Create a matcher with no patterns
const matcher = createMatcher([]);

// This should return false but returns true
console.log(matcher('any-file.txt')); // Expected: false, Actual: true
console.log(matcher('another-file.md')); // Expected: false, Actual: true
```

### Expected behavior

When no patterns are provided (empty array), the matcher should not match any strings. An empty pattern list logically means "match nothing", similar to how an empty whitelist works.

### Additional context

This is causing issues in my plugin where I'm trying to exclude files based on user-provided patterns. When users don't provide any exclusion patterns, all files are being excluded instead of none.

---
Repository: /testbed
