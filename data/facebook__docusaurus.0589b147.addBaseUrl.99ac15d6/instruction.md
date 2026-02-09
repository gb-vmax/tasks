# Bug Report

### Describe the bug

I'm experiencing an issue with `useBaseUrl` where it's not handling URLs correctly anymore. It seems like the function is now adding the base URL even when it shouldn't, or in some cases returning undefined/incorrect values.

### Reproduction

```js
import useBaseUrl from '@docusaurus/useBaseUrl';

// This returns undefined now instead of the original URL
const url1 = useBaseUrl('');

// Local anchor links are getting base URL prepended incorrectly
const url2 = useBaseUrl('#section');

// This is also behaving strangely
const url3 = useBaseUrl('/docs');
```

### Expected behavior

- Empty strings should be returned as-is
- Local anchor URLs (starting with `#`) should not have the base URL added to them
- The function should correctly determine when to add or skip adding the base URL

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems to have broken after a recent update. The base URL logic appears to be inverted or the conditions for when to apply it have changed unexpectedly.

---
Repository: /testbed
