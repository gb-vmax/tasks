# Bug Report

### Describe the bug

Footnote references and definitions are not linking correctly in blog posts. When clicking on a footnote reference (like `[^1]`), it doesn't navigate to the corresponding footnote definition, and the reference/definition IDs appear to be mismatched.

### Reproduction

Create a blog post with footnotes:

```markdown
---
title: Test Post
---

This is some text with a footnote reference[^1].

Here's another reference[^2].

[^1]: This is the first footnote.
[^2]: This is the second footnote.
```

When the page renders, clicking on the footnote reference `[^1]` doesn't jump to the footnote definition. Inspecting the HTML shows that the IDs don't match - the reference has one hash suffix while the definition has a different one.

### Expected behavior

Footnote references should link to their corresponding definitions. The generated IDs for references and definitions should match so that clicking a reference navigates to the correct footnote.

### System Info
- Docusaurus version: latest
- Plugin: docusaurus-plugin-content-blog

---
Repository: /testbed
