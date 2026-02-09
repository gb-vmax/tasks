# Bug Report

### Describe the bug

I'm experiencing an issue with client-side redirects in Docusaurus where query parameters are not being preserved during redirects. When redirecting from a page with search params (e.g., `?foo=bar`), the query string gets lost in the redirect target.

### Reproduction

```js
// Set up a redirect from /old-page to /new-page
// Navigate to /old-page?param=value

// Expected: redirect to /new-page?param=value
// Actual: redirect to /new-page (query params are dropped)
```

Steps to reproduce:
1. Configure a redirect in your Docusaurus config
2. Navigate to the source URL with query parameters (e.g., `/old-page?search=test`)
3. Observe that after redirect, the query parameters are missing from the URL

### Expected behavior

Query parameters and search strings should be forwarded to the redirect target URL, similar to how hash/anchor fragments are handled.

### System Info

- Docusaurus version: latest
- Browser: Chrome/Firefox (both affected)

This seems like a regression as I believe this used to work in earlier versions. The redirect happens but the query string portion of the URL is not being preserved.

---
Repository: /testbed
