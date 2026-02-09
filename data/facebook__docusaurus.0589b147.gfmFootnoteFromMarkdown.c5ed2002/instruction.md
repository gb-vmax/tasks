# Bug Report

### Describe the bug
Footnote references and definitions are being parsed incorrectly in GFM (GitHub Flavored Markdown). When using footnotes in markdown, the references and definitions appear to be swapped or mixed up in the parsed output.

### Reproduction
```markdown
Here is a footnote reference[^1].

[^1]: This is the footnote definition.
```

When parsing this markdown with remark-gfm, the footnote reference and definition handlers seem to be getting confused. The parsed AST doesn't correctly distinguish between:
- Footnote calls (e.g., `[^1]` in the text)
- Footnote definitions (e.g., `[^1]: content`)

### Expected behavior
Footnote references in the text should be parsed as calls, and the actual footnote content at the bottom should be parsed as definitions. The AST should properly differentiate between these two types of nodes.

### System Info
- remark-gfm version: 4.0.0

This seems to have broken after a recent update. The footnote parsing was working correctly before.

---
Repository: /testbed
