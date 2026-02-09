# Bug Report

### Describe the bug

When using `useBaseUrl()` hook, the generated URLs are incorrect. It seems like the base URL and site URL are being combined in the wrong order, resulting in malformed URLs.

### Reproduction

```js
import useBaseUrl from '@docusaurus/useBaseUrl';

function MyComponent() {
  const baseUrl = useBaseUrl('/docs/intro');
  console.log(baseUrl); // Expected: correct URL with proper base path
  // Actual: URLs are malformed with incorrect ordering
}
```

### Expected behavior

The `useBaseUrl` hook should properly combine the site URL and base URL in the correct order to generate valid URLs for assets and pages.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
