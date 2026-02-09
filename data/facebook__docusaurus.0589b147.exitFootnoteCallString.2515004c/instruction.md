# Bug Report

### Describe the bug

I'm experiencing an issue with footnote references in markdown parsing. The `label` and `identifier` properties appear to be swapped - the label is getting the normalized/lowercased value while the identifier is getting the raw label text.

### Reproduction

When parsing markdown with footnotes like this:

```markdown
Here is a footnote reference[^1]

[^1]: Footnote text
```

The resulting AST node for the footnote reference has:
- `identifier` set to the display label (e.g., "1")
- `label` set to the normalized identifier (e.g., "1")

This seems backwards from what I'd expect.

### Expected behavior

Based on the property names, I would expect:
- `label` should contain the human-readable label text
- `identifier` should contain the normalized/lowercased identifier for lookups

The current behavior has these reversed, which makes it confusing when trying to work with the parsed AST.

### System Info
- remark-gfm version: 4.0.0

---
Repository: /testbed
