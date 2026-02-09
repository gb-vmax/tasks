# Bug Report

### Describe the bug

After a recent update, internal links in my Docusaurus site are no longer being matched correctly. All routes appear to be broken and I'm getting broken link warnings/errors even though the pages exist and the links are valid.

### Reproduction

1. Create a Docusaurus site with multiple pages
2. Add internal links between pages (e.g., `[Link](/docs/page)`)
3. Build the site
4. All internal links are reported as broken even though the target pages exist

For example, if I have a page at `/docs/getting-started` and link to it from another page:

```md
[Getting Started](/docs/getting-started)
```

The link is flagged as broken during the build process, even though the page exists in the routes.

### Expected behavior

Internal links to existing pages should be recognized as valid and not reported as broken links.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems to have started happening after the most recent update. The site was working fine before.

---
Repository: /testbed
