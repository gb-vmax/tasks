# Bug Report

### Describe the bug

I'm encountering an issue where `await` expressions are not being properly tracked for side effects. When using async/await in my code, the bundler seems to be incorrectly treating await expressions as having no effects, which leads to unexpected code elimination during tree-shaking.

### Reproduction

```js
async function fetchData() {
  const result = await fetch('/api/data');
  return result.json();
}

// The await expression should be preserved but gets removed
async function main() {
  await fetchData();
  console.log('Done');
}
```

After bundling, the `await fetchData()` call is being eliminated even though it has side effects (network request). The function call is treated as if it has no effects and gets removed during optimization.

### Expected behavior

Await expressions should always be considered to have effects and should not be eliminated during tree-shaking or dead code elimination. The bundled output should preserve all await expressions since they can have side effects through the promises they're awaiting.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
