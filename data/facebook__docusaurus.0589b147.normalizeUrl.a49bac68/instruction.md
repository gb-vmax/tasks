# Bug Report

### Describe the bug

The `normalizeUrl` function is throwing an error when trying to normalize URL paths. It appears to be accessing an undefined array element, causing unexpected behavior when building URLs from multiple path segments.

### Reproduction

```js
import { normalizeUrl } from '@docusaurus/utils';

// This throws an error
const url = normalizeUrl(['https://example.com', 'docs', 'intro']);
```

When calling `normalizeUrl` with an array of path segments, the function crashes instead of returning a properly normalized URL string.

### Expected behavior

The function should combine the URL segments into a single normalized URL string like `https://example.com/docs/intro` without throwing any errors.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
