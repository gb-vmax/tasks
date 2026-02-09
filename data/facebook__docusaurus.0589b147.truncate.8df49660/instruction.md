# Bug Report

### Describe the bug

The blog post truncation feature is not working as expected. When using the truncate marker (e.g., `<!--truncate-->`) in blog posts, the content that appears in the blog list view is incorrect - it shows everything **after** the truncate marker instead of everything **before** it.

### Reproduction

Create a blog post with the following content:

```markdown
---
title: My Blog Post
---

This is the intro text that should appear in the list view.

<!--truncate-->

This is the full content that should only appear on the individual post page.
```

When viewing the blog list page, the excerpt shows "This is the full content..." instead of "This is the intro text...".

### Expected behavior

The blog list view should display only the content **before** the `<!--truncate-->` marker. The content after the marker should only be visible when viewing the full blog post.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
