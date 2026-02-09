# Bug Report

### Describe the bug

I'm experiencing an issue with redirect URL generation in the client-redirects plugin. When I configure a redirect with a path starting with a single forward slash `/`, the URL is not being properly normalized with the baseUrl. This results in broken redirects.

### Reproduction

```js
// In docusaurus.config.js
module.exports = {
  baseUrl: '/my-site/',
  plugins: [
    [
      '@docusaurus/plugin-client-redirects',
      {
        redirects: [
          {
            from: '/old-page',
            to: '/new-page',  // This should become /my-site/new-page
          },
        ],
      },
    ],
  ],
};
```

The redirect is created but the `to` URL doesn't include the baseUrl prefix, so clicking on `/old-page` redirects to `/new-page` instead of `/my-site/new-page`.

### Expected behavior

When using a path starting with `/` in the `to` field, it should be treated as a site-relative path and the baseUrl should be prepended automatically. The redirect should work correctly and navigate to `/my-site/new-page`.

### Additional context

This seems to have broken recently. Previously, paths starting with `/` were being normalized correctly with the baseUrl.

---
Repository: /testbed
