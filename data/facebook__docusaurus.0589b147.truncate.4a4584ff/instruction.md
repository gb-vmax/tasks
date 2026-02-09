# Bug Report

### Describe the bug

The blog post truncation feature is not working correctly. When using the truncate marker (e.g., `<!--truncate-->`), the content that appears in the blog list view is showing the wrong portion of the post.

### Reproduction

```md
---
title: My Blog Post
---

This is the intro content that should appear in the list view.

<!--truncate-->

This is the detailed content that should only appear on the full post page.
```

### Expected behavior

The blog list should show only the content **before** the truncate marker:
```
This is the intro content that should appear in the list view.
```

### Actual behavior

The blog list is showing the content **after** the truncate marker instead:
```
This is the detailed content that should only appear on the full post page.
```

It seems like the truncation logic is reversed - it's keeping the wrong part of the content.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
