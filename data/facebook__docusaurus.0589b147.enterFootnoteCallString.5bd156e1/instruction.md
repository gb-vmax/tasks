# Bug Report

### Describe the bug

Footnote references in GFM (GitHub Flavored Markdown) are not being parsed correctly. The label/identifier for footnotes appears to be empty or missing when processing footnote calls.

### Reproduction

```markdown
Here is a sentence with a footnote[^1].

[^1]: This is the footnote content.
```

When parsing this markdown, the footnote reference should capture the label "1" but instead it's coming through as empty. The footnote structure is created but without the proper identifier linking it to the footnote definition.

### Expected behavior

The footnote reference should contain the label/identifier (e.g., "1") so it can be properly linked to the corresponding footnote definition. The parsed AST should have a footnoteReference node with identifier: "1" and label: "1".

### System Info
- remark-gfm version: 4.0.0

---
Repository: /testbed
