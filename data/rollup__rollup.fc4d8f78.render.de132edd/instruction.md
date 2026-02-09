# Bug Report

### Describe the bug

When using `import.meta.ROLLUP_FILE_URL_<referenceId>` in my code, the generated output includes extra code that shouldn't be there. It looks like the replacement is not overwriting the correct range - the original `import.meta.ROLLUP_FILE_URL_*` expression is still partially present in the output along with the replacement code.

### Reproduction

```js
// input.js
const assetUrl = import.meta.ROLLUP_FILE_URL_0;
console.log(assetUrl);
```

After bundling, the output contains both the original meta property access and the replacement code, instead of just the replacement.

### Expected behavior

The `import.meta.ROLLUP_FILE_URL_<referenceId>` should be completely replaced with the resolved file URL code. The original meta property expression should not appear in the output at all.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
