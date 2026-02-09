# Bug Report

### Describe the bug

When using spread/rest operators in MDX files, the generated JavaScript output has incorrect syntax with the spread operator (`...`) appearing in the wrong position. This causes syntax errors when trying to use the compiled MDX.

### Reproduction

```js
// In an MDX file, using rest parameters:
function example(...args) {
  return args;
}

// Or using spread in destructuring:
const [...items] = array;
```

After compilation, the spread operator `...` appears after the identifier instead of before it, resulting in invalid JavaScript like `args...` instead of `...args`.

### Expected behavior

The compiled output should have valid JavaScript syntax with the spread/rest operator (`...`) positioned before the identifier, not after it.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
