# Bug Report

### Describe the bug

When using `applyTrailingSlash()` with paths that contain URL fragments (hash anchors) in the middle of the path, the function is not correctly preserving the hash and query parameters. The path gets truncated or malformed after applying the trailing slash logic.

### Reproduction

```js
import applyTrailingSlash from '@docusaurus/utils-common';

const path = '/docs/intro#section?query=test';
const result = applyTrailingSlash(path, {
  trailingSlash: true,
  baseUrl: '/'
});

console.log(result);
// Expected: '/docs/intro/#section?query=test'
// Actual: Incorrect output - hash and query params not preserved correctly
```

### Expected behavior

The function should:
1. Apply trailing slash logic only to the pathname portion
2. Preserve the hash fragment and query parameters in their original positions
3. Not modify paths that have anchors in the middle

### Additional context

This seems to affect paths where the hash appears somewhere other than at the very beginning of the string. Paths like `#anchor` work fine, but paths with content before the hash are processed incorrectly.

---
Repository: /testbed
