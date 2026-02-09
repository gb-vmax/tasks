# Bug Report

### Describe the bug

I'm encountering an issue with code fence metadata parsing in markdown. When parsing fenced code blocks that include metadata (info string after the language), the metadata appears to be getting assigned to the wrong node in the AST.

### Reproduction

```js
const markdown = `
\`\`\`javascript someMetadata
console.log('test');
\`\`\`
`;

// Parse the markdown
const ast = parse(markdown);

// The meta property ends up in an unexpected location
console.log(ast); // meta is not where it should be
```

When parsing a fenced code block with metadata like:
````markdown
```js metadata-info
code here
```
````

The `meta` property seems to be getting attached to the parent node instead of the code block node itself.

### Expected behavior

The `meta` field should be properly assigned to the code block node that contains the fenced code, not to a different level in the AST hierarchy.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
