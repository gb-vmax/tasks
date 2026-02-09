# Bug Report

### Describe the bug

I'm experiencing an issue with redirect file path generation in the client redirects plugin. When I configure redirects with `trailingSlash` set to `false`, the redirect files are being created in unexpected locations that don't match the intended behavior.

### Reproduction

```js
// docusaurus.config.js
module.exports = {
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
  trailingSlash: false,
};
```

When building the site with `trailingSlash: false`, the redirect files are not being placed in the correct directory structure. For example, a redirect from `/old-page` should create a file at `/old-page.html` but the actual file path generated seems incorrect.

Additionally, for paths ending with `.html` (like `/docs/guide.html`), the redirect file placement appears to be inverted from what's expected based on the `trailingSlash` configuration.

### Expected behavior

- With `trailingSlash: false`, redirect files should be created as `/path.html` 
- With `trailingSlash: true`, redirect files for `.html` paths should handle the special case properly
- The file naming should respect the fileName variable when constructing the final path

### System Info

- Docusaurus version: 2.x
- Node version: 18.x

---
Repository: /testbed
