# Bug Report

### Describe the bug

I'm experiencing an issue with footnote definitions in markdown parsing. When a document contains footnotes, the parser seems to be processing them incorrectly, leading to unexpected behavior in the AST structure.

### Reproduction

```js
const markdown = `
Here is some text with a footnote[^1].

[^1]: This is the footnote definition.
`;

const ast = parseMarkdown(markdown);
// The AST structure is malformed
```

When parsing markdown with footnote definitions, the resulting AST appears to have structural issues. The footnote definition nodes don't seem to be properly closed or positioned in the tree.

### Expected behavior

Footnote definitions should be parsed correctly and produce a well-formed AST with proper node hierarchy. The footnote definition should be a single, properly structured node in the output.

### System Info
- remark-gfm version: 4.0.0
- Node version: 18.x

---
Repository: /testbed
