# Bug Report

### Describe the bug
When parsing fenced code blocks with metadata in markdown, the metadata is not being attached to the correct node. The metadata appears to be going to the wrong location in the AST structure.

### Reproduction
```js
const markdown = `
\`\`\`js title="example.js"
console.log('hello');
\`\`\`
`;

// Parse the markdown
const result = remark().parse(markdown);

// The code block node doesn't have the metadata in the expected location
console.log(result.children[0].meta); // Expected: 'title="example.js"'
```

### Expected behavior
The `meta` property should be properly set on the code block node when parsing fenced code blocks with metadata (like language hints followed by additional metadata).

### System Info
- remark version: 15.0.1
- Node.js version: Latest

---
Repository: /testbed
