# Bug Report

### Describe the bug

The `normalizeUrl` function is incorrectly handling leading slashes, causing absolute paths to lose their initial slash. This breaks URL normalization for paths that should start with `/`.

### Reproduction

```js
import {normalizeUrl} from '@docusaurus/utils';

// This should return '/docs/intro' but returns 'docs/intro'
const result = normalizeUrl(['/docs', 'intro']);
console.log(result); // Expected: '/docs/intro', Actual: 'docs/intro'

// Another example
const result2 = normalizeUrl(['/api', '/users']);
console.log(result2); // Expected: '/api/users', Actual: 'api/users'
```

### Expected behavior

When the first URL segment starts with a slash (indicating an absolute path), the normalized result should preserve that leading slash. The function should return `/docs/intro` instead of `docs/intro`.

### Additional context

This seems to have started happening recently. The function is removing leading slashes from absolute paths which breaks routing and navigation in my Docusaurus site. Links that should point to `/docs/...` are now pointing to relative paths instead.

---
Repository: /testbed
