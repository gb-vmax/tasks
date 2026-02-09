# Bug Report

### Describe the bug

Footnote references in blog posts are not linking correctly to their definitions. When clicking on a footnote reference (e.g., `[^1]`), it either doesn't navigate to the corresponding definition or navigates to the wrong footnote.

### Reproduction

Create a blog post with multiple footnotes:

```markdown
# My Blog Post

This is some text with a footnote[^1] and another one[^2].

[^1]: First footnote definition
[^2]: Second footnote definition
```

When the page renders, clicking on the footnote references doesn't properly link to the definitions. The IDs seem to be mismatched between the reference and definition elements.

### Expected behavior

Footnote references should have matching identifiers with their corresponding definitions so that clicking a reference scrolls to and highlights the correct definition. Both the reference and definition should share the same unique identifier (with the same suffix appended).

### Additional context

This appears to be affecting all blog posts with footnotes. The footnote functionality was working correctly in previous versions.

---
Repository: /testbed
