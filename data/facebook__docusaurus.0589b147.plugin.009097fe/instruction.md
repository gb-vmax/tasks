# Bug Report

### Describe the bug

Footnote references are not being linked correctly in blog posts. The footnote markers in the text don't connect to their corresponding definitions at the bottom of the page, making them non-functional.

### Reproduction

Create a blog post with footnotes:

```markdown
---
title: Test Post
---

This is a sentence with a footnote reference[^1].

[^1]: This is the footnote definition.
```

After building, the footnote reference in the text doesn't link to the definition. Clicking on the footnote marker does nothing, and the reference and definition appear to have mismatched IDs.

### Expected behavior

Footnote references should be properly linked to their definitions. Clicking on a footnote marker (e.g., `[1]`) should jump to the corresponding footnote definition at the bottom of the page.

### System Info

- Docusaurus version: latest
- Plugin: @docusaurus/plugin-content-blog

---
Repository: /testbed
