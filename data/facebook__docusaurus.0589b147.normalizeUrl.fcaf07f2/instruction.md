# Bug Report

### Describe the bug

The `normalizeUrl` function is removing leading slashes from URLs when it shouldn't. After a recent change, URLs that should start with a forward slash (like absolute paths) are being returned without the leading slash.

### Reproduction

```js
import {normalizeUrl} from '@docusaurus/utils';

// This should return '/docs/intro' but returns 'docs/intro'
const result = normalizeUrl(['/docs', 'intro']);
console.log(result); // Expected: '/docs/intro', Actual: 'docs/intro'

// Another example
const result2 = normalizeUrl(['/api/v1', 'users']);
console.log(result2); // Expected: '/api/v1/users', Actual: 'api/v1/users'
```

### Expected behavior

The function should preserve the leading slash for absolute paths. URLs that start with `/` should still start with `/` after normalization.

### Additional context

This is affecting route generation in my Docusaurus site. Links that should be absolute paths are now being treated as relative paths, breaking navigation.

---
Repository: /testbed
