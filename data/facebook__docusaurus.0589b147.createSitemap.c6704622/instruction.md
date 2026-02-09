# Bug Report

### Describe the bug

The sitemap plugin is generating sitemaps with only excluded routes instead of included routes. All pages that should be in the sitemap are missing, while pages that should be excluded (like 404 pages, specific paths marked for exclusion) are appearing in the generated sitemap.

### Reproduction

```js
// docusaurus.config.js
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

After building the site, the generated `sitemap.xml` only contains:
- `/tags/...` pages
- `/admin/...` pages

But is missing all the regular content pages that should be included.

### Expected behavior

The sitemap should contain all routes EXCEPT the ones matching the ignore patterns. The excluded routes should not appear in the sitemap.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
