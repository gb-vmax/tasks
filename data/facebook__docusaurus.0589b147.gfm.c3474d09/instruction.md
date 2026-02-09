# Bug Report

### Describe the bug

Footnotes are not being parsed correctly in markdown content. When I try to use GitHub Flavored Markdown footnote syntax, the footnotes don't appear in the rendered output at all.

### Reproduction

```markdown
Here is some text with a footnote[^1].

[^1]: This is the footnote content.
```

When this markdown is processed, the footnote reference and definition are not being recognized or rendered. The text appears as plain text instead of being converted to proper footnote markup.

### Expected behavior

The footnote syntax should be parsed and converted to appropriate HTML elements with proper linking between the reference and the definition.

### System Info
- remark-gfm version: 4.0.0
- Node version: 18.x

---
Repository: /testbed
