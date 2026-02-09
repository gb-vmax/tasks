# Bug Report

### Describe the bug

When parsing markdown code blocks (fenced code blocks with triple backticks), the parser is producing incorrect node types. Instead of generating `code` nodes for code blocks, it appears to be creating `text` nodes, which breaks proper rendering of code blocks.

### Reproduction

```js
const remark = require('remark');
const markdown = `
\`\`\`javascript
const foo = 'bar';
console.log(foo);
\`\`\`
`;

const ast = remark.parse(markdown);
console.log(ast.children[0].type); // Expected: 'code', Actual: 'text'
```

### Expected behavior

Code blocks should be parsed as `code` type nodes with the appropriate `lang`, `meta`, and `value` properties. The `value` property should contain the code content as a string, not `null`.

### Additional context

This seems to affect any fenced code block in markdown. The parsed AST structure is incorrect, which would cause issues for any plugins or renderers that expect proper `code` nodes.

---
Repository: /testbed
