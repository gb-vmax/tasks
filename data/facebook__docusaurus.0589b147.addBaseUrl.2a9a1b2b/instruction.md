# Bug Report

### Describe the bug

I'm experiencing an issue with `useBaseUrl()` where it's duplicating the base URL in the generated paths. When I pass a URL that already contains the base URL, it gets added again, resulting in incorrect double paths like `/baseUrl/baseUrl/path`.

### Reproduction

```js
// Assuming baseUrl is '/docs/'
const url1 = useBaseUrl('/docs/getting-started');
// Expected: '/docs/getting-started'
// Actual: '/docs/docs/getting-started'

const url2 = useBaseUrl('getting-started');
// This one works fine: '/docs/getting-started'
```

The problem occurs when the URL already starts with the base URL. Instead of recognizing that the base URL is already present and leaving it as-is, it prepends it again.

### Expected behavior

`useBaseUrl()` should detect when the base URL is already present in the path and avoid adding it twice. URLs that already start with the base URL should be returned unchanged (or normalized, but not duplicated).

### System Info
- Docusaurus version: Latest
- Node version: 18.x

---
Repository: /testbed
