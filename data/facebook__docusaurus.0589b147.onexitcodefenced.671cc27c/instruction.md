# Bug Report

### Describe the bug

I'm experiencing an issue with fenced code blocks in markdown parsing. When parsing markdown with fenced code blocks (using triple backticks), the content appears to be getting assigned to the wrong node in the AST.

### Reproduction

```js
const markdown = `
# Title

\`\`\`js
const example = 'test';
\`\`\`

Some text after
`;

const result = remark.parse(markdown);
// The code block value ends up in an unexpected location in the AST
```

When I parse markdown containing fenced code blocks, the code content doesn't appear where it should in the resulting syntax tree. It seems like the parser is looking at the wrong stack position when trying to set the code block's value.

### Expected behavior

The fenced code block should be properly parsed and its content should be assigned to the correct code node in the AST. The value should contain the code between the fences with leading/trailing newlines stripped.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
