# Bug Report

### Describe the bug

I'm encountering an issue where the AST node traversal seems to be completely broken. When parsing code, child nodes are not being properly identified or visited, which causes the entire tree walking mechanism to fail.

### Reproduction

```js
// Any code that requires AST traversal will fail
import { parse } from 'rollup';

const code = `
  const foo = {
    bar: 'test'
  };
`;

const ast = parse(code);
// Child nodes are not being traversed correctly
// Properties that should be identified as child nodes are being skipped
```

### Expected behavior

The parser should correctly identify and traverse all child nodes in the AST. Object properties and nested structures should be properly visited during tree walking operations.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently. The AST traversal was working fine before, but now it's like the tree structure isn't being recognized at all.

---
Repository: /testbed
