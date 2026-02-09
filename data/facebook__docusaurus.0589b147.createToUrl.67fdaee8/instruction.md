# Bug Report

### Describe the bug

I'm experiencing an issue with redirect URLs in the client redirects plugin. When I configure a redirect with a path that starts with `/`, it's not being properly prefixed with the `baseUrl`. The redirect destination ends up being incorrect - it just uses the raw path instead of combining it with the base URL.

### Reproduction

```js
// docusaurus.config.js
module.exports = {
  baseUrl: '/my-site/',
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

With the above config, when navigating to `/my-site/old-page`, the redirect goes to `/new-page` instead of `/my-site/new-page`. This breaks the redirect when the site is deployed with a non-root base URL.

### Expected behavior

The redirect should respect the `baseUrl` configuration and redirect to `/my-site/new-page` when the `to` path starts with `/`.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
