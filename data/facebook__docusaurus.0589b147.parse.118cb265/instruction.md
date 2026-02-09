# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where the parser seems to be ignoring custom program nodes passed through options. When I provide a custom `program` node via `options.program`, the parser appears to create a new node instead of using the one I provided.

### Reproduction

```js
const customProgramNode = {
  type: 'Program',
  start: 0,
  end: 0,
  body: [],
  sourceType: 'module'
};

const parser = new Parser({
  program: customProgramNode
}, inputCode, 0);

const result = parser.parse();

// Expected: result should be the customProgramNode I passed in
// Actual: result is a different node object
console.log(result === customProgramNode); // false
```

### Expected behavior

When passing a custom `program` node through `options.program`, the parser should use that exact node object as the root of the AST, not create a new one. This is important for cases where we need to maintain references to specific node objects or when integrating with other tools that expect the same node instance.

### System Info

- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
