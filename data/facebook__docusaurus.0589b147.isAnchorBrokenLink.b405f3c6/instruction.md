# Bug Report

### Describe the bug

Anchor links are not being validated correctly. When I use links with hash fragments (like `#section-id`), the broken link checker doesn't properly detect whether the anchor exists on the target page or not.

### Reproduction

```md
<!-- In page.md -->
## My Section

[Link to section](#my-section)
[Link to non-existent section](#does-not-exist)
```

Expected behavior:
- `#my-section` should be valid
- `#does-not-exist` should be reported as broken

Actual behavior:
- Valid anchor links are being reported as broken
- Invalid anchor links are not being detected

### Additional context

This seems to affect all anchor links in my documentation. The broken link checker is not correctly matching anchor IDs to the actual headings/anchors present on the pages.

Version: Latest from main branch

---
Repository: /testbed
