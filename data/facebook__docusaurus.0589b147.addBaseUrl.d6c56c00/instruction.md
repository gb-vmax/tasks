# Bug Report

### Describe the bug

The `useBaseUrl` hook is incorrectly prepending the base URL to paths that already contain it, resulting in duplicated base URLs in the final path.

### Reproduction

```js
import useBaseUrl from '@docusaurus/useBaseUrl';

// Assuming baseUrl is '/docs/'
const url1 = useBaseUrl('/docs/getting-started');
// Expected: '/docs/getting-started'
// Actual: '/docs/docs/getting-started'

const url2 = useBaseUrl('/docs');
// Expected: '/docs/'
// Actual: '/docs/docs'
```

When passing a URL that already starts with the configured base URL, the function adds the base URL again instead of returning the path as-is.

### Expected behavior

The function should detect when a URL already starts with the base URL and avoid adding it twice. URLs that already include the base URL should be returned unchanged.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
