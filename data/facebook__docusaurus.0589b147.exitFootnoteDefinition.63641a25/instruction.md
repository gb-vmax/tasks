# Bug Report

### Describe the bug

I'm experiencing an issue with footnote definitions not being processed correctly. When parsing markdown with footnote definitions, the parser seems to skip or ignore the footnote content entirely.

### Reproduction

```js
const markdown = `
Here is some text with a footnote[^1].

[^1]: This is the footnote definition.
`;

const result = parseMarkdown(markdown);
// The footnote definition is not properly included in the output
```

When I try to parse markdown containing footnote definitions, the definitions don't appear in the resulting AST or the footnote references don't link correctly to their definitions.

### Expected behavior

Footnote definitions should be properly parsed and included in the output. The footnote reference should be able to link to its corresponding definition.

### System Info
- remark-gfm version: 4.0.0
- Node version: Latest

---
Repository: /testbed
