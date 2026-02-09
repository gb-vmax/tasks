# Bug Report

### Describe the bug

The sitemap is not being generated correctly - it's including routes that should be excluded. I'm seeing 404 pages, routes matching my ignore patterns, and pages with noindex meta tags all appearing in the sitemap.xml file.

### Reproduction

```js
// docusaurus.config.js
module.exports = {
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        sitemap: {
          ignorePatterns: ['/tags/**', '/admin/**'],
        },
      },
    ],
  ],
};
```

After building the site, the generated sitemap includes:
- The 404.html page
- Routes under `/tags/` and `/admin/` that should be ignored
- Pages that have `<meta name="robots" content="noindex">` in their head

### Expected behavior

The sitemap should exclude:
1. The 404 page
2. Any routes matching the ignore patterns
3. Pages with noindex meta tags

All of these should be filtered out and not appear in the final sitemap.xml.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
