# Bug Report

### Describe the bug

When rendering MDX content that contains paragraphs, the paragraph elements are not being created correctly. The content still displays but without the proper paragraph structure/wrapping.

### Reproduction

```mdx
This is a paragraph.

This is another paragraph.
```

When this MDX is processed, the paragraphs don't get wrapped in the expected paragraph tokens/elements. The text content appears but the paragraph structure is missing from the output.

### Expected behavior

Each paragraph block should be properly wrapped with paragraph enter/exit tokens so that the final output includes the correct paragraph elements in the AST/rendered output.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
