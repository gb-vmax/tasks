# Bug Report

### Describe the bug

After a recent update, blog post front matter validation is failing. When trying to build the site, I'm getting errors about front matter structure even though my blog posts haven't changed.

### Reproduction

Create a blog post with standard front matter:

```md
---
title: My Blog Post
date: 2024-01-15
tags: [react, docusaurus]
draft: false
---

Blog content here...
```

When building the site, the front matter validation throws an error. The same blog posts worked fine before the update.

### Expected behavior

The blog post front matter should validate successfully and the site should build without errors. The front matter structure is standard and follows the documented format.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
