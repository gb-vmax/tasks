# Bug Report

### Describe the bug

I'm encountering an issue with markdown parsing where indented code blocks are not being recognized correctly. It seems like the parser is treating lazy continuation lines incorrectly, causing code blocks to be parsed as regular paragraphs instead.

### Reproduction

```js
const markdown = `
Some paragraph text.

    indented code block
    more code here
    
Another paragraph.
`;

// Parse the markdown
const result = parse(markdown);

// Expected: code block node
// Actual: paragraph node with the indented text
```

When I parse markdown with indented code blocks (4 spaces), they're not being detected as code blocks. Instead, they're being treated as part of the surrounding paragraph or as regular text.

### Expected behavior

Indented code blocks (lines starting with 4+ spaces) should be parsed as code block nodes, not as regular paragraph text. The parser should correctly distinguish between lazy continuation lines and actual indented code.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This seems to have started happening recently. Not sure if this is related to recent changes in the lazy continuation handling logic.

---
Repository: /testbed
