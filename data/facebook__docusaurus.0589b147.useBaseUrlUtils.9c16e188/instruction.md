# Bug Report

### Describe the bug

The `useBaseUrl` hook is generating incorrect URLs. When I try to use it with absolute URLs, the output is completely wrong - it seems like the base URL and site URL are being combined in the wrong order.

### Reproduction

```js
import { useBaseUrl } from '@docusaurus/useBaseUrl';

function MyComponent() {
  const baseUrl = useBaseUrl('/docs/intro');
  console.log(baseUrl); // Expected: correct URL, Actual: malformed URL
}
```

When I have a site with:
- siteUrl: `https://example.com`
- baseUrl: `/myapp/`

And I call `useBaseUrl('/docs/intro')`, the resulting URL has the parameters in the wrong order or something. The URL structure looks messed up.

### Expected behavior

The hook should correctly combine the base URL with the provided path to generate a valid URL. The site URL and base URL should be applied in the correct order.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems to have broken recently, possibly after a recent update. The URLs were working fine before.

---
Repository: /testbed
