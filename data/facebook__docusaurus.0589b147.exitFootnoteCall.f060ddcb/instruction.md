# Bug Report

### Describe the bug

I'm experiencing an issue with footnote rendering in GFM (GitHub Flavored Markdown). When parsing markdown with footnotes, the parser seems to get stuck or produce malformed output. The footnote references in the document aren't being properly closed/exited, which causes the AST structure to be incorrect.

### Reproduction

```js
const markdown = `
Here is some text with a footnote[^1].

[^1]: This is the footnote content.
`;

const result = parseMarkdown(markdown);
// The AST structure is malformed - footnote call nodes are not properly handled
```

When I try to parse markdown containing footnote references, the resulting abstract syntax tree doesn't have the correct structure. It seems like the parser is entering nodes but not properly exiting them, leading to an unbalanced tree structure.

### Expected behavior

Footnote references should be properly parsed and the AST should have a balanced structure with correctly matched enter/exit calls for footnote nodes.

### System Info
- remark-gfm version: 4.0.0
- Node version: 18.x

---
Repository: /testbed
