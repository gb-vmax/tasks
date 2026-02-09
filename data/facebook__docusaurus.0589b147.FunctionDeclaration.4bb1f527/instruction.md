# Bug Report

### Describe the bug

I'm encountering an issue with function declaration code generation where anonymous functions are being rendered incorrectly. When generating code for function declarations that have an `id` (i.e., named functions), the function name is not being output properly.

### Reproduction

```js
// Given a function declaration AST node with an id:
const node = {
  type: 'FunctionDeclaration',
  id: { name: 'myFunction' },
  async: false,
  generator: false,
  params: [],
  body: { type: 'BlockStatement', body: [] }
}

// The generated output is missing the function name
// Expected: "function myFunction() {}"
// Actual: "function () {}"
```

### Expected behavior

Named function declarations should include their function name in the generated code output. The function name should appear between the `function` keyword and the parameter list.

### Additional context

This seems to affect all named function declarations. Anonymous function expressions might work correctly, but regular named functions are being treated as if they have no identifier.

---
Repository: /testbed
