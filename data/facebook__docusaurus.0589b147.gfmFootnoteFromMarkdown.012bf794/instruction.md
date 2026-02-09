# Bug Report

### Describe the bug
Footnote references and definitions are not being parsed correctly in GFM (GitHub Flavored Markdown). When using footnotes in markdown content, the reference links and definition blocks appear to be swapped or incorrectly mapped, causing footnotes to not render properly.

### Reproduction
```markdown
Here is some text with a footnote reference[^1].

[^1]: This is the footnote definition.
```

When parsing this markdown:
1. The footnote reference `[^1]` in the text is not properly linked
2. The footnote definition at the bottom is not correctly associated with its reference
3. The parsed AST structure shows mismatched node types between calls and definitions

### Expected behavior
Footnote references should correctly link to their corresponding definitions. The parser should properly distinguish between:
- Footnote calls/references (inline `[^1]` in text)
- Footnote definitions (block-level `[^1]: content`)

### System Info
- remark-gfm version: 4.0.0

This appears to have broken footnote functionality entirely. Any markdown documents using footnotes are now being parsed incorrectly.

---
Repository: /testbed
