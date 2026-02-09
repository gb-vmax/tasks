# Bug Report

### Describe the bug

The sitemap plugin is generating an empty sitemap or including the wrong routes. It seems like the filtering logic for excluded routes is inverted - routes that should be excluded are being included, and routes that should be included are being excluded.

### Reproduction

```js
// Configuration with ignored paths
module.exports = {
  url: 'https://example.com',
  baseUrl: '/',
  plugins: [
    [
      '@docusaurus/plugin-sitemap',
      {
        ignorePatterns: ['/tags/**', '/admin/**'],
      },
    ],
  ],
};
```

With this configuration:
1. Routes like `/tags/getting-started` and `/admin/dashboard` appear in the sitemap
2. Regular routes like `/docs/intro` and `/blog` are missing from the sitemap

### Expected behavior

Routes matching the `ignorePatterns` should be excluded from the sitemap, and all other valid routes should be included. The sitemap should contain all public pages except those explicitly ignored.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This is causing SEO issues as search engines are indexing pages that should be hidden and missing pages that should be discoverable.

---
Repository: /testbed
