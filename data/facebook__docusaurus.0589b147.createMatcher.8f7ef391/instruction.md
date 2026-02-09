# Bug Report

### Describe the bug

When using `createMatcher` with an empty patterns array, it returns a matcher function that incorrectly matches all strings instead of matching nothing.

### Reproduction

```js
import { createMatcher } from '@docusaurus/utils';

// Create a matcher with no patterns
const matcher = createMatcher([]);

// This should return false but returns true
console.log(matcher('some-file.md')); // Expected: false, Actual: true
console.log(matcher('any-string')); // Expected: false, Actual: true
```

### Expected behavior

When `createMatcher` is called with an empty array, the returned matcher function should return `false` for all inputs (since there are no patterns to match against). Currently it returns `true` for everything.

This breaks filtering logic where an empty pattern list should mean "match nothing" rather than "match everything".

### System Info
- @docusaurus/utils version: latest
- Node version: 18.x

---
Repository: /testbed
