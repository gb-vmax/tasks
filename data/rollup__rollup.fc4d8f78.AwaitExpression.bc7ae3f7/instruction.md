# Bug Report

### Describe the bug

I'm encountering an issue with top-level await detection in my project. It appears that await expressions inside nested arrow functions or regular functions are incorrectly being treated as top-level awaits, causing the bundler to mark modules as using top-level await when they shouldn't be.

### Reproduction

```js
// This should NOT be treated as top-level await
async function fetchData() {
  const result = await fetch('/api/data');
  return result;
}

// Neither should this
const getData = async () => {
  return await someAsyncOperation();
};
```

After bundling, the module is incorrectly flagged as using top-level await, which causes issues with module loading in environments that don't support it.

### Expected behavior

Await expressions that are inside function bodies (arrow functions or regular functions) should not be considered top-level awaits. Only await expressions that are directly in the module scope should trigger the `usesTopLevelAwait` flag.

### Additional context

This seems to have started happening recently. The bundler is now treating all await expressions as top-level, regardless of whether they're actually at the top level or nested inside functions.

---
Repository: /testbed
