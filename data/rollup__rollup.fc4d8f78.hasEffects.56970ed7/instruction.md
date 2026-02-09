# Bug Report

### Describe the bug

I'm experiencing an issue where `await` expressions are not being properly tracked for side effects. When using async/await in my code, the bundler seems to be incorrectly optimizing away or not properly handling the await expressions, leading to unexpected behavior in the output.

### Reproduction

```js
async function fetchData() {
  const response = await fetch('https://api.example.com/data');
  return response.json();
}

async function main() {
  await fetchData();
  console.log('Done');
}
```

When bundling this code, the await expression doesn't seem to be recognized as having effects, which causes issues with the generated output. The async operations are being treated as if they have no side effects.

### Expected behavior

Await expressions should be properly recognized as having effects since they:
- Pause execution flow
- Can potentially throw errors
- Have observable timing effects

The bundler should preserve these await expressions and not optimize them away or treat them as effect-free operations.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
