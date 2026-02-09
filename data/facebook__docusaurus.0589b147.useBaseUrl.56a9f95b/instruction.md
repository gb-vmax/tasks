# Bug Report

### Describe the bug

I'm experiencing an issue with `useBaseUrl()` where passing options causes URLs to behave incorrectly. When I provide any options to the hook, the leading slash gets stripped from my URL and the options themselves are cleared out, which breaks the expected URL generation.

### Reproduction

```js
import useBaseUrl from '@docusaurus/useBaseUrl';

// This returns an incorrect URL - leading slash is removed
const url1 = useBaseUrl('/docs/intro', { absolute: true });
// Expected: /baseUrl/docs/intro (or absolute version)
// Actual: baseUrldocs/intro (malformed)

// This also doesn't work as expected
const url2 = useBaseUrl('/img/logo.png', { forcePrependBaseUrl: true });
// The options are being ignored/cleared
```

### Expected behavior

When passing options to `useBaseUrl()`, the URL should be processed correctly with the leading slash preserved, and the options should be passed through to `withBaseUrl()` so they can take effect.

### System Info

- Docusaurus version: latest
- Node version: 18.x

This seems to have started recently. The hook works fine when called without options, but as soon as I add any option parameter, the URL generation breaks.

---
Repository: /testbed
