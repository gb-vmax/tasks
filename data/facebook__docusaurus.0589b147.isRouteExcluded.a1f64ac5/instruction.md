# Bug Report

### Describe the bug

The sitemap is not being generated correctly - it appears to be excluding most or all routes that should be included. Only 404 pages seem to be processed, while regular pages are being filtered out.

### Reproduction

1. Set up a Docusaurus site with multiple pages
2. Configure the sitemap plugin with default settings
3. Build the site
4. Check the generated sitemap.xml

Expected: All public pages should appear in the sitemap (excluding 404s and explicitly ignored patterns)
Actual: The sitemap is mostly empty or only contains unexpected routes

### Steps to reproduce

```js
// docusaurus.config.js
module.exports = {
  plugins: [
    [
      '@docusaurus/plugin-sitemap',
      {
        // default config
      },
    ],
  ],
};
```

After building, the sitemap doesn't include normal pages like `/docs/intro`, `/blog`, etc. that should be indexed.

### Expected behavior

The sitemap should include all routes except:
- 404 error pages
- Routes matching ignore patterns
- Routes with noindex meta tags

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
