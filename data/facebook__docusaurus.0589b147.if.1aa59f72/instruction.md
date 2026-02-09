# Bug Report

### Describe the bug

I'm experiencing an issue with the blog plugin where I can't use the `authors` front matter at all. Whenever I try to use the new `authors` field in my blog post front matter, I get an error telling me not to mix `authors` with the legacy `author_*` fields, even though I'm not using any legacy fields.

### Reproduction

Create a blog post with only the `authors` front matter (no legacy `author_*` fields):

```md
---
title: My Blog Post
authors: john
---

Blog content here...
```

This throws an error:
```
To declare blog post authors, use the 'authors' front matter in priority. Mix 'authors' with other existing 'author_*' front matter. Choose one or the other, not both at the same time.
```

### Expected behavior

The blog post should render correctly when using only the `authors` front matter without any legacy author fields. The error should only appear when actually mixing both the new `authors` field and the old `author_*` fields together.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
