# Bug Report

### Describe the bug

I'm experiencing an issue with code fence metadata handling in markdown parsing. When using fenced code blocks with metadata (the part after the language identifier), the metadata seems to be incorrectly assigned to the wrong node in the AST.

### Reproduction

```js
const markdown = `
\`\`\`javascript meta="some metadata"
const code = 'example';
\`\`\`
`;

// Parse the markdown
const result = parseMarkdown(markdown);

// The metadata appears in the wrong location in the AST
// Expected: metadata on the code block node
// Actual: metadata seems to be assigned incorrectly
```

### Expected behavior

When parsing a fenced code block with metadata, the `meta` property should be correctly attached to the code block node. The metadata should be accessible at the proper level in the AST structure.

### Additional context

This seems to affect how code fence metadata is processed during the exit handler. The metadata information is being placed on an unexpected node in the stack, which breaks downstream processing that relies on the correct AST structure.

---
Repository: /testbed
