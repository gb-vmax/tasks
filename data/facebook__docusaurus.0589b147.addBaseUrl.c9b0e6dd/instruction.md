# Bug Report

### Describe the bug

I'm experiencing an issue with `useBaseUrl` where URLs are getting the base URL prepended multiple times, resulting in malformed paths. It seems like the logic that prevents double-adding the base URL is broken.

### Reproduction

```js
import useBaseUrl from '@docusaurus/useBaseUrl';

// Assuming baseUrl is '/docs/'
const url = useBaseUrl('/docs/getting-started');

// Expected: '/docs/getting-started'
// Actual: '/docs/docs/getting-started'
```

Also, URLs with protocols (like `https://example.com`) are now getting the base URL prepended when they shouldn't be:

```js
const externalUrl = useBaseUrl('https://example.com/page');

// Expected: 'https://example.com/page'
// Actual: '/docs/https://example.com/page'
```

### Expected behavior

- URLs that already start with the base URL should not have it prepended again
- External URLs with protocols should be returned as-is without base URL prepending
- Local anchor links (starting with `#`) should be returned unchanged

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
