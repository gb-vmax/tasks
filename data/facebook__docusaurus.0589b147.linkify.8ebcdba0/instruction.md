# Bug Report

### Describe the bug

The `linkify` function is not processing markdown links correctly. When I use relative links in my documentation, they remain unchanged instead of being converted to their permalink equivalents.

### Reproduction

```md
<!-- In my markdown file -->
[Check out this page](./other-page.md)
[Another link](../category/another-doc.md)
```

After processing, the links stay as `./other-page.md` and `../category/another-doc.md` instead of being converted to the proper permalinks like `/docs/other-page` or `/docs/category/another-doc`.

### Expected behavior

The markdown links should be transformed to their corresponding permalinks based on the `sourceToPermalink` mapping. The function should process the content and return the updated markdown with converted links.

### Additional context

This seems to have broken recently. The links are just staying in their original form and not being processed at all.

---
Repository: /testbed
