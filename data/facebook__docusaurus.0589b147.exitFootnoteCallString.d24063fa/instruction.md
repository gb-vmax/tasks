# Bug Report

### Describe the bug

I'm experiencing an issue with footnote references in GFM (GitHub Flavored Markdown) parsing. When parsing markdown with footnote references, the identifier is not being generated correctly from the label text.

### Reproduction

```markdown
Here is some text with a footnote reference[^1].

[^1]: This is the footnote content.
```

When parsing this markdown, the footnote reference identifier should be derived from the label (in this case "1"), but instead it seems to be using the wrong token serialization which results in incorrect identifier generation.

### Expected behavior

The footnote reference node should have:
- `label`: The display label from the reference (e.g., "1")
- `identifier`: A normalized, lowercase version of the label (e.g., "1")

Both should be derived from the same label text to ensure consistency.

### Additional context

This appears to affect how footnote references are matched with their definitions. The identifier normalization is not being applied to the correct source, which could cause footnote links to break when the label contains special characters or formatting.

---
Repository: /testbed
