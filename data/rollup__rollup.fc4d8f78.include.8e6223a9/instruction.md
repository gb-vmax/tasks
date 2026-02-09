# Bug Report

### Describe the bug

I'm encountering an issue with `await` expressions where the code seems to be included incorrectly during tree-shaking. When using top-level await, some parts of the awaited expression are being unexpectedly removed or duplicated in the output bundle.

### Reproduction

```js
// Input code
const data = await fetch('https://api.example.com/data')
  .then(res => res.json())
  .then(data => data.value);

console.log(data);
```

After bundling, the output doesn't behave as expected - it seems like the await expression's argument is being processed incorrectly, leading to either missing code or incorrect inclusion in the final bundle.

### Expected behavior

The entire await expression and its argument should be properly included in the bundle when top-level await is used. The bundled output should preserve the complete expression chain.

### System Info
- Rollup version: latest
- Node version: 18.x

This appears to be related to how the inclusion logic handles await expressions. The issue seems to manifest when the awaited expression has nested method calls or complex expressions.

---
Repository: /testbed
