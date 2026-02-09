# Bug Report

### Describe the bug

When parsing source code into an AST, the parser is failing to return valid program nodes. Instead of returning the parsed AST structure, it's throwing errors even for valid JavaScript/TypeScript code.

### Reproduction

```js
import { parse } from 'rollup';

const code = `
  export const foo = 'bar';
  console.log(foo);
`;

// This should return a valid AST but throws an error instead
const ast = parse(code);
```

### Expected behavior

The parser should successfully convert the buffer to an AST and return a valid program node for syntactically correct code. Only invalid/malformed code should trigger error handling.

### Additional context

This appears to affect all parsing operations. Even simple, valid code that should parse without issues is being rejected. The parser seems to be treating valid program nodes as errors.

---
Repository: /testbed
