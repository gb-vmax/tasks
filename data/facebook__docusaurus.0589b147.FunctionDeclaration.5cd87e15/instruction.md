# Bug Report

### Describe the bug

I'm encountering an issue with the code generator when handling async generator functions. The output seems to be missing the `async` keyword for async generator functions, which results in invalid JavaScript syntax.

### Reproduction

When trying to generate code for an async generator function like this:

```js
async function* myAsyncGenerator() {
  yield 1;
  yield 2;
}
```

The generator outputs:

```js
function* myAsyncGenerator() {
  yield 1;
  yield 2;
}
```

Notice that the `async` keyword is missing from the output.

### Expected behavior

The code generator should preserve the `async` keyword for async generator functions and output:

```js
async function* myAsyncGenerator() {
  yield 1;
  yield 2;
}
```

### Additional context

This appears to affect function declarations specifically. Regular async functions (non-generator) seem to work fine, and regular generator functions (non-async) also work correctly. The issue only manifests when both `async` and `generator` properties are true.

---
Repository: /testbed
