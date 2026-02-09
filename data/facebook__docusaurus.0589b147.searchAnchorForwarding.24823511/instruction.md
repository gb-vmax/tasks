# Bug Report

### Describe the bug

Redirects are not preserving URL query parameters (search params) when redirecting to a new page. The redirect works but any query string attached to the original URL gets dropped during the redirect process.

### Reproduction

```js
// Set up a redirect from /old-page to /new-page
// Navigate to: /old-page?utm_source=newsletter&ref=email

// Expected: redirect to /new-page?utm_source=newsletter&ref=email
// Actual: redirect to /new-page (query params are lost)
```

Steps to reproduce:
1. Configure a redirect in docusaurus.config.js
2. Navigate to the old URL with query parameters
3. Observe that the query parameters are not forwarded to the new URL

This is breaking our analytics tracking since we rely on UTM parameters being preserved across redirects. The hash/anchor part of the URL seems to work fine, but query strings are being dropped.

### Expected behavior

Both query parameters and hash fragments should be preserved when redirecting, just like they were in previous versions.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
