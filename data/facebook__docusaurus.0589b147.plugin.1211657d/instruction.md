# Bug Report

### Describe the bug

I'm experiencing an issue with footnote references in blog posts. When I have footnotes in my markdown content, the footnote references and definitions don't match up correctly - they seem to be using different ID suffixes.

### Reproduction

Create a blog post with footnotes:

```markdown
---
title: Test Post
---

This is a test paragraph with a footnote reference[^1].

[^1]: This is the footnote definition.
```

The footnote reference link and the footnote definition end up with mismatched identifiers, so clicking on the footnote reference doesn't jump to the correct definition.

### Expected behavior

Footnote references and their corresponding definitions should have matching identifiers so that they link together properly. When clicking a footnote reference, it should navigate to the correct footnote definition.

### System Info

- Docusaurus version: latest
- Plugin: @docusaurus/plugin-content-blog

---
Repository: /testbed
