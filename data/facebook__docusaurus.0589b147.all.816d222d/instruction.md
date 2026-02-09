# Bug Report

### Describe the bug

I'm encountering an issue with markdown processing where the output is missing content or producing unexpected results. It seems like the parser is skipping over some nodes when converting markdown to HTML.

### Reproduction

When processing markdown with multiple child nodes, some elements appear to be getting skipped:

```js
// Example markdown structure with sequential nodes
const markdown = `
First paragraph
Second paragraph
Third paragraph
`;

// After conversion, one or more paragraphs are missing from the output
```

The issue seems to occur when iterating through child nodes - the first node in the tree doesn't get processed correctly, or the loop starts at the wrong position.

### Expected behavior

All child nodes should be processed and included in the output. Every paragraph/element in the source markdown should appear in the converted HTML.

### System Info
- remark-rehype version: 11.0.0
- Node version: latest

---
Repository: /testbed
