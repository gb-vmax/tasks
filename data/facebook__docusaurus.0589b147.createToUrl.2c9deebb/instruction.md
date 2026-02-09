# Bug Report

### Describe the bug

I'm experiencing an issue with redirect URLs in the client-redirects plugin. When I configure redirects with absolute paths (starting with `/`), they're not being generated correctly. The URLs seem to be getting normalized in an unexpected way.

### Reproduction

```js
// In docusaurus.config.js
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
]
```

When I set up a redirect with an absolute path like `/new-page`, the generated redirect doesn't work as expected. The URL handling appears to be inverted - paths that should be treated as absolute are being processed differently.

### Expected behavior

Redirects with absolute paths (starting with `/`) should be properly normalized with the base URL. Relative paths should also be handled correctly by combining them with the base URL.

For example:
- `to: '/new-page'` should normalize to `baseUrl + '/new-page'`
- `to: 'new-page'` (relative) should also normalize to `baseUrl + 'new-page'`

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
