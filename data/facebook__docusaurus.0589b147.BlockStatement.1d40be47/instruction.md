# Bug Report

### Describe the bug

When generating code from AST nodes with block statements, the indentation for the first statement in a block is missing. This causes the first line inside curly braces to not be properly indented while subsequent statements are indented correctly.

### Reproduction

```js
// Given an AST with a BlockStatement containing multiple statements
const ast = {
  type: 'BlockStatement',
  body: [
    { type: 'ExpressionStatement', ... },
    { type: 'ExpressionStatement', ... },
    { type: 'ReturnStatement', ... }
  ]
}

// When generating code from this AST
const output = generate(ast)

// The output looks like:
// {
// firstStatement();  // <- Missing indentation!
//   secondStatement();
//   return value;
// }
```

### Expected behavior

All statements within a block should have consistent indentation:

```js
{
  firstStatement();
  secondStatement();
  return value;
}
```

Currently only statements after the first one are properly indented, making the generated code look malformed.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
