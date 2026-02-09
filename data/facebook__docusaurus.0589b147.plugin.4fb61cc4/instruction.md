# Bug Report

### Describe the bug

Footnote references and definitions are not linking correctly when using markdown footnotes in blog posts. The footnote links appear to be broken - clicking on a footnote reference doesn't jump to the corresponding definition at the bottom of the page.

### Reproduction

Create a blog post with footnotes:

```markdown
---
title: Test Post
---

This is some text with a footnote[^1].

Here's another footnote[^2].

[^1]: First footnote definition
[^2]: Second footnote definition
```

When the page renders, the footnote reference links and definition IDs don't match up properly, so clicking on the superscript numbers doesn't navigate to the footnote text at the bottom.

### Expected behavior

Clicking on a footnote reference (e.g., `[^1]`) should scroll to and highlight the corresponding footnote definition at the bottom of the page. The `id` and `href` attributes should match correctly.

### System Info
- Docusaurus version: latest
- Browser: Chrome/Firefox

---
Repository: /testbed
