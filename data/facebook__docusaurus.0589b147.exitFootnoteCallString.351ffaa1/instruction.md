# Bug Report

### Describe the bug

Footnote references are not being parsed correctly when the footnote label contains special characters or formatting. The identifier seems to be generated incorrectly, causing mismatches between footnote definitions and their references.

### Reproduction

```markdown
Here is a footnote reference[^note-1].

[^note-1]: This is the footnote content.
```

When parsing this markdown with remark-gfm, the footnote reference doesn't link properly to its definition. The identifier generated for the reference doesn't match the identifier for the definition.

### Expected behavior

The footnote reference should correctly link to its corresponding definition. The identifier should be normalized consistently from the label text, allowing footnotes with special characters (like hyphens, underscores, etc.) to work properly.

### System Info
- remark-gfm version: 4.0.0
- Node version: 18.x

---
Repository: /testbed
