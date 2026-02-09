# Bug Report

### Describe the bug

Markdown links are not being processed/converted in documentation files. The links remain in their original format instead of being transformed to their permalink versions.

### Reproduction

When building a docs site with markdown files containing relative links like:

```md
Check out [this guide](../other-doc.md) for more info.
```

The link stays as `../other-doc.md` instead of being converted to the proper permalink format (e.g., `/docs/other-doc`).

Steps to reproduce:
1. Create a markdown file with relative links to other docs
2. Build the site
3. The rendered output shows the raw markdown link paths instead of converted permalinks

### Expected behavior

Markdown links should be automatically converted to their corresponding permalinks based on the `sourceToPermalink` mapping. The linkify function should process the file content and return the transformed content with updated links.

### Additional context

This seems to have broken recently. The links were working fine before and were being properly converted to permalinks.

---
Repository: /testbed
