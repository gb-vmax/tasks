# Bug Report

### Describe the bug

I'm encountering an issue with code block parsing where fenced code blocks are not being recognized correctly. The parser seems to be treating code blocks as something else entirely, and the content is not being preserved as expected.

### Reproduction

```js
const markdown = `
\`\`\`javascript
const foo = 'bar';
console.log(foo);
\`\`\`
`;

const result = parse(markdown);
// The code block node has incorrect type and missing value
```

When parsing markdown with fenced code blocks, the resulting AST node doesn't have the correct structure. The type field is wrong and the actual code content appears to be lost.

### Expected behavior

Code blocks should be parsed into nodes with:
- `type: "code"`
- `value` containing the actual code content as a string
- Proper `lang` and `meta` fields

Instead, the parser is creating nodes with an incorrect type and the value is not being set properly.

### System Info
- remark version: 15.0.1
- Node version: Latest

This is breaking our markdown rendering pipeline. Any help would be appreciated!

---
Repository: /testbed
