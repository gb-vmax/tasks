# Bug Report

### Describe the bug

I'm experiencing an issue with code block parsing where the generated AST nodes have incorrect types. When parsing fenced code blocks in markdown, the node type is being set to `"codeFlow"` instead of the expected `"code"` type.

### Reproduction

```js
const processor = remark();
const tree = processor.parse('```js\nconsole.log("test")\n```');

// The code block node has wrong type
console.log(tree.children[0].type); // outputs "codeFlow" but should be "code"
```

### Expected behavior

Code blocks should generate nodes with `type: "code"` to match the mdast specification. The current output breaks compatibility with tools expecting standard mdast nodes.

Additionally, the `value` field is being set to `null` instead of an empty string `""`, which also differs from the expected mdast format.

### System Info
- remark version: 15.0.1
- Node.js version: 18.x

---
Repository: /testbed
