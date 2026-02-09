# Bug Report

### Describe the bug

I'm experiencing an issue with code fence metadata in markdown parsing. When I have a fenced code block with metadata (the part after the language identifier), the metadata seems to be incorrectly assigned to the wrong property or node.

### Reproduction

```js
const markdown = `
\`\`\`javascript meta="some metadata"
console.log('test');
\`\`\`
`;

// Parse the markdown
const result = parseMarkdown(markdown);

// Expected: code block node should have a 'meta' property with "some metadata"
// Actual: the metadata appears to be going to the wrong place or property
```

When parsing fenced code blocks like the above, the metadata that should be attached to the code block node doesn't seem to be in the right place. The structure of the parsed AST looks incorrect.

### Expected behavior

The code fence metadata should be properly attached to the code block node as a `meta` property, not assigned to a different property or a different node in the tree.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
