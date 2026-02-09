# Bug Report

### Describe the bug

I'm experiencing an issue with redirect URLs in the client-redirects plugin. When I configure a redirect with a path that starts with `/`, the generated redirect URL is incorrect - it's just using the raw path without properly combining it with the base URL.

### Reproduction

```js
// docusaurus.config.js
module.exports = {
  baseUrl: '/docs/',
  plugins: [
    [
      '@docusaurus/plugin-client-redirects',
      {
        redirects: [
          {
            from: '/old-page',
            to: '/new-page',
          },
        ],
      },
    ],
  ],
};
```

When navigating to `/docs/old-page`, the redirect doesn't work correctly. It seems like the `to` path isn't being properly resolved with the baseUrl.

### Expected behavior

The redirect should correctly combine the baseUrl with the target path, so `/old-page` with baseUrl `/docs/` should redirect to `/docs/new-page`.

### Additional context

This seems to affect redirects where the `to` field starts with a `/`. Relative paths without the leading slash might work differently but I haven't tested that scenario extensively.

---
Repository: /testbed
