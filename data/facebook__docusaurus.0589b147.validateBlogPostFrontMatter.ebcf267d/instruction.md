# Bug Report

### Describe the bug

Blog post frontmatter validation is completely broken. When I try to build my site with blog posts, the frontmatter validation throws errors even for valid frontmatter fields.

### Reproduction

Create a blog post with standard frontmatter:

```md
---
title: My Blog Post
date: 2024-01-15
authors: [john]
tags: [javascript, react]
---

# My Blog Post

Content here...
```

When building the site, the validation fails and throws an error about the frontmatter schema.

### Expected behavior

The blog post frontmatter should validate correctly and the site should build without errors. Valid frontmatter fields like `title`, `date`, `authors`, and `tags` should be accepted.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems to have broken recently - my blog posts were working fine before. Now none of them validate properly.

---
Repository: /testbed
