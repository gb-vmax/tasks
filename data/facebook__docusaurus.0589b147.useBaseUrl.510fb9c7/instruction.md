# Bug Report

### Describe the bug

When using `useBaseUrl()` with custom options (like `forcePrependBaseUrl` or `absolute`), the options are being ignored and the function behaves as if called with default/empty options instead.

### Reproduction

```js
import useBaseUrl from '@docusaurus/useBaseUrl';

// Try to use with custom options
const url1 = useBaseUrl('/docs/intro', { forcePrependBaseUrl: true });
const url2 = useBaseUrl('/docs/intro', { absolute: true });

// Both return the same result as if options were {}
// Expected: url1 and url2 should respect the provided options
```

### Expected behavior

The `useBaseUrl` hook should respect the options passed to it. When I pass `{ forcePrependBaseUrl: true }` or `{ absolute: true }`, these options should be applied when generating the URL.

Currently it seems like any options I pass are just ignored completely.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
