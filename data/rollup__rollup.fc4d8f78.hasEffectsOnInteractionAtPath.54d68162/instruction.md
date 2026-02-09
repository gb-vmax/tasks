# Bug Report

### Describe the bug

I'm encountering an issue with tree-shaking async functions. When using async functions in my code, the bundler is incorrectly removing code that should be kept. It seems like the tree-shaking logic isn't properly detecting side effects for async functions.

### Reproduction

```js
async function fetchData() {
  const response = await fetch('/api/data');
  return response.json();
}

fetchData().then(data => {
  console.log(data);
});
```

After bundling, the code that should handle the promise chain gets removed even though it has side effects. The `.then()` handler is being treated as if it has no effects when it clearly does.

### Expected behavior

The bundler should recognize that async functions and their promise chains have side effects and should not be removed during tree-shaking. The `.then()` callback should be preserved in the output.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
