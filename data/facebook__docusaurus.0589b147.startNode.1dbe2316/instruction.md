# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where node positions are being incorrectly initialized. When parsing MDX content, the AST nodes seem to have wrong position information - specifically the start and end positions appear to be swapped or incorrect.

### Reproduction

```js
// Parse any MDX content
const ast = parse(`
# Hello World

Some content here
`);

// Check the position of the first node
console.log(ast.children[0].position);
// Expected: start position should be at the beginning of the node
// Actual: position information is incorrect
```

### Expected behavior

AST nodes should have accurate position information with `start` reflecting the beginning of the node and `end` reflecting the end of the node. This is important for source mapping, error reporting, and tooling that relies on accurate position data.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
