# Bug Report

### Describe the bug

The sitemap plugin is generating empty sitemaps or not including routes that should be present. It seems like the route filtering logic is inverted - routes that should be included are being excluded and vice versa.

### Reproduction

```js
// Configure sitemap plugin with ignorePatterns
module.exports = {
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

After building the site, the generated sitemap is either empty or only contains the routes that were supposed to be excluded (like `/tags/**` and `/admin/**`), while all the normal pages are missing.

### Expected behavior

The sitemap should include all routes EXCEPT those matching the `ignorePatterns`. Routes like `/docs/intro`, `/blog`, etc. should be in the sitemap, while `/tags/**` and `/admin/**` should be excluded.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
