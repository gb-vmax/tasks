# Bug Report

### Describe the bug

I'm experiencing an issue with footnote definitions in GFM (GitHub Flavored Markdown). When parsing markdown with footnotes, the footnote definitions are being incorrectly converted to footnote references instead of maintaining their proper type.

### Reproduction

```markdown
Here's some text with a footnote[^1].

[^1]: This is the footnote definition.
```

When this markdown is parsed and converted, the footnote definition `[^1]` is being treated as a footnote reference rather than a definition. This causes the AST structure to be incorrect and breaks the rendering of footnotes.

### Expected behavior

Footnote definitions should maintain their type as `footnoteDefinition` in the AST, not be converted to `footnoteReference`. The parser should correctly distinguish between:
- Footnote references (inline): `[^1]`
- Footnote definitions (block): `[^1]: definition text`

### System Info
- remark-gfm version: 4.0.0

This seems to have broken footnote handling entirely. Any markdown with footnote definitions now fails to render properly.

---
Repository: /testbed
