# Bug Report

### Describe the bug

I'm encountering an issue with the spread operator (`...`) when used with rest elements in destructuring. The spread operator appears to be generated in the wrong position, causing syntax errors in the output.

### Reproduction

When using rest parameters in function arguments or destructuring patterns, the generated code has incorrect syntax:

```js
// Input code with rest parameter
function example(...args) {
  console.log(args);
}

// Or destructuring with rest
const [first, ...rest] = array;
```

The generated output places the spread operator after the identifier instead of before it, resulting in invalid JavaScript syntax.

### Expected behavior

The spread operator (`...`) should appear **before** the rest element identifier, not after. The correct syntax should be:
- `...args` (not `args...`)
- `...rest` (not `rest...`)

### System Info
- Package: @mdx-js/mdx@3.0.0
- Node version: Latest

This seems to have broken code generation for any MDX files that use rest parameters or rest elements in destructuring patterns.

---
Repository: /testbed
