# Bug Report

### Describe the bug

I'm experiencing an issue with blog post front matter validation in Docusaurus. When I include an `id` field in my blog post's front matter, it seems to be getting stripped out or not properly validated. Additionally, if there are any validation errors in the front matter, they're being silently swallowed instead of being reported.

### Reproduction

Create a blog post with the following front matter:

```markdown
---
title: My Blog Post
id: custom-blog-id
date: 2024-01-15
---

Post content here...
```

The `id` field appears to be removed during processing, and the blog post doesn't use my custom ID.

Also, if I intentionally add invalid front matter:

```markdown
---
title: My Blog Post
invalidField: someValue
date: not-a-valid-date
---
```

No validation errors are thrown - the invalid data just gets passed through silently.

### Expected behavior

1. The `id` field in front matter should be preserved and properly validated
2. Invalid front matter should throw clear validation errors instead of being silently ignored

### System Info

- Docusaurus version: Latest
- Node version: 18.x

This seems like it might be a recent regression as my blog posts with custom IDs were working fine before.

---
Repository: /testbed
