# Bug Report

### Describe the bug

When using the `authors` front matter in blog posts, I'm getting an error even when I'm not mixing it with legacy `author_*` fields. The error message says I shouldn't mix the two approaches, but I'm only using the new `authors` field.

### Reproduction

Create a blog post with only the `authors` front matter:

```md
---
title: My Blog Post
authors: john
---

Post content here...
```

When building the site, I get this error:

```
Error: To declare blog post authors, use the 'authors' front matter in priority.
Mix 'authors' with other existing 'author_*' front matter. Choose one or the other, not both at the same time.
```

### Expected behavior

The blog post should build successfully when using only the `authors` field without any legacy `author_*` fields. The error should only appear when actually mixing both approaches.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
