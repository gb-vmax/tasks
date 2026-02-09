# Bug Report

### Describe the bug

When using `useBaseUrl()` with absolute URLs (http:// or https://), the function is stripping the protocol and forcing the URL to be treated as relative, which breaks external links.

### Reproduction

```js
import useBaseUrl from '@docusaurus/useBaseUrl';

// This returns an incorrect URL without the protocol
const externalUrl = useBaseUrl('https://example.com/path');
// Expected: 'https://example.com/path'
// Actual: something like '/baseUrl/example.com/path'

// Same issue with http://
const httpUrl = useBaseUrl('http://example.com');
// Gets converted to a relative path instead of staying absolute
```

### Expected behavior

Absolute URLs (starting with `http://` or `https://`) should be returned as-is without modification. The function should only process relative URLs by adding the base URL prefix.

External links should remain external and not be converted to relative paths.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
