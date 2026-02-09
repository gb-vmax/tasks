# Bug Report

### Describe the bug

When declaring async generator functions, the output is incorrectly formatted. The function declaration appears to be missing the generator syntax (`*`) when both `async` and `generator` flags are present.

### Reproduction

```js
// Async generator function
async function* myAsyncGenerator() {
  yield 1;
  yield 2;
}
```

After processing through the code generator, the output appears to be malformed - it seems like async generator functions are not being handled correctly. The generator asterisk (`*`) is not appearing in the output when the function is both async and a generator.

### Expected behavior

Async generator functions should be properly formatted with both the `async` keyword and the `function*` syntax, like:
```js
async function* myAsyncGenerator() {
  // ...
}
```

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
