# Bug Report

### Describe the bug

When using the redirect plugin, the redirect pages are not being generated correctly. The redirect functionality appears to be broken - instead of redirecting to the target URL, the page shows undefined or doesn't redirect at all.

### Reproduction

Create a redirect configuration in your Docusaurus config:

```js
redirects: [
  {
    from: '/old-page',
    to: '/new-page',
  },
]
```

When navigating to `/old-page`, the redirect doesn't work as expected. The page either shows an error or doesn't redirect to the target URL.

### Expected behavior

The redirect page should properly redirect users from the old URL to the new URL specified in the configuration. The `toUrl` parameter should be correctly passed to the redirect page template so the redirect can function.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
