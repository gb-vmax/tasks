# Bug Report

### Describe the bug

I'm experiencing an issue with `useBaseUrl` where URLs are being constructed incorrectly. When I use `useBaseUrl` with the `absolute` option, the site URL is being appended in the wrong position, and the base URL logic seems inverted.

### Reproduction

```js
// With baseUrl = '/docs/' and siteUrl = 'https://example.com'

const url1 = useBaseUrl('/getting-started', { absolute: true });
// Expected: 'https://example.com/docs/getting-started'
// Getting: '/docs/getting-startedhttps://example.com'

const url2 = useBaseUrl('/api/overview');
// Expected: '/docs/api/overview'
// Getting: '/api/overview' (base URL not added)
```

### Steps to reproduce

1. Configure a site with a baseUrl (e.g., `/docs/`)
2. Try to generate an absolute URL using `useBaseUrl` with `{ absolute: true }`
3. Notice the siteUrl appears at the end instead of the beginning
4. Also notice that relative URLs that should have baseUrl prepended don't get it

### Expected behavior

- When `absolute: true`, the URL should be formatted as `siteUrl + baseUrl + path`
- The baseUrl should be prepended to paths that don't already have it
- URLs that already start with the baseUrl shouldn't have it duplicated

This seems to have broken recently and is affecting link generation across the site.

---
Repository: /testbed
