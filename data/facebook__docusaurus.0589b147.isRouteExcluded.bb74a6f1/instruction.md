# Bug Report

### Describe the bug

The sitemap plugin is not excluding routes correctly. Routes that should be excluded from the sitemap (like 404 pages and pages with noindex meta tags) are being included, and routes that should be included are being excluded.

### Reproduction

1. Create a Docusaurus site with the sitemap plugin enabled
2. Add some pages with `noindex` meta tags in the front matter:
```md
---
noindex: true
---
# My Page
```
3. Build the site and check the generated sitemap
4. Pages with `noindex: true` appear in the sitemap (they shouldn't)
5. Regular pages that should be in the sitemap are missing

### Expected behavior

- 404 pages should be excluded from sitemap
- Pages matching ignore patterns should be excluded
- Pages with noindex meta tags should be excluded
- All other pages should be included in the sitemap

### Additional context

This seems to affect sitemap generation logic. The filtering doesn't work as expected and the wrong pages end up in the sitemap file.

---
Repository: /testbed
