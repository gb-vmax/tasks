# Bug Report

### Describe the bug

I'm encountering an issue with variable declarations in MDX files after a recent update. When parsing variable statements, the parser seems to be skipping tokens and producing incorrect AST node types.

### Reproduction

```jsx
const MyComponent = () => {
  var x = 1;
  let y = 2;
  const z = 3;
  
  return <div>{x + y + z}</div>
}
```

When this code is parsed, the variable declarations are not being handled correctly. The parser appears to be producing `VariableStatement` nodes instead of the expected `VariableDeclaration` nodes, and it's not consuming the initial token properly.

### Expected behavior

Variable declarations (`var`, `let`, `const`) should be parsed correctly and produce proper `VariableDeclaration` AST nodes. The parser should advance through tokens in the correct sequence.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

This seems to have broken after updating the vendored parser code. The variable statement parsing logic doesn't match the expected behavior anymore.

---
Repository: /testbed
