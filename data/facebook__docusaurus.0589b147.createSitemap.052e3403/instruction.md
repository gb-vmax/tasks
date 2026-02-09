# Bug Report

### Describe the bug

The sitemap generation is producing incorrect results. Routes that should be included in the sitemap are being excluded, and the trailing slash behavior appears to be inverted.

### Reproduction

When building a site with the sitemap plugin configured:

```js
// docusaurus.config.js
module.exports = {
  url: 'https://example.com',
  baseUrl: '/',
  trailingSlash: true,
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        sitemap: {
          changefreq: 'weekly',
          priority: 0.5,
        },
      },
    ],
  ],
};
```

After building the site, the generated `sitemap.xml`:
1. Only contains routes that were meant to be excluded (opposite of expected behavior)
2. URLs have incorrect trailing slash handling - when `trailingSlash: true` is set, URLs in the sitemap don't have trailing slashes, and vice versa

### Expected behavior

- Routes that are not excluded should appear in the sitemap
- When `trailingSlash: true`, sitemap URLs should end with `/`
- When `trailingSlash: false`, sitemap URLs should not end with `/`

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
