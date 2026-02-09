# Bug Report

### Describe the bug

I'm experiencing an issue with footnote references in markdown parsing. When using footnote syntax like `[^1]`, the footnote label is not being captured correctly. Instead of buffering the content properly, it appears that the internal state is being flushed prematurely, causing the footnote reference to lose its label text.

### Reproduction

```markdown
Here is some text with a footnote reference[^note1].

[^note1]: This is the footnote content.
```

When parsing this markdown:
1. The footnote reference `[^note1]` is encountered
2. The label "note1" should be captured and stored
3. Instead, the label appears to be empty or not properly associated with the reference

### Expected behavior

The footnote reference should correctly capture and store the label "note1" so it can be properly linked to the corresponding footnote definition. The parsed AST should contain a footnoteReference node with the identifier set to "note1".

### System Info
- remark-gfm version: 4.0.0
- Environment: Node.js

---
Repository: /testbed
