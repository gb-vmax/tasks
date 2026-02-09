# Bug Report

### Describe the bug

I'm experiencing an issue with footnote references in GFM (GitHub Flavored Markdown) parsing. When parsing markdown with footnote references, the identifier normalization seems to be behaving incorrectly - it's not converting identifiers to lowercase as expected.

### Reproduction

```markdown
Here's a footnote reference[^MyFootnote].

[^MyFootnote]: This is the footnote content.
```

When parsing this markdown, the footnote reference identifier should be normalized to lowercase (`myfootnote`), but it appears to retain the original casing (`MyFootnote`). This causes issues when trying to match footnote references with their definitions, especially when the reference and definition use different casing.

### Expected behavior

Footnote identifiers should be normalized to lowercase to ensure case-insensitive matching between references and definitions. For example, `[^MyFootnote]` and `[^myfootnote]` should both resolve to the same footnote definition.

### System Info
- remark-gfm version: 4.0.0

---
Repository: /testbed
