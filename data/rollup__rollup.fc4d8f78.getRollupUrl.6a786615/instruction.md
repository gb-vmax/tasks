# Bug Report

### Describe the bug

The `getRollupUrl` function is encoding URL snippets incorrectly, which breaks links to the Rollup documentation. When passing a snippet path like `guide/en/`, the function now encodes the forward slashes and other characters, resulting in malformed URLs like `https://rollupjs.org/guide%2Fen%2F` instead of `https://rollupjs.org/guide/en/`.

### Reproduction

```js
const url = getRollupUrl('guide/en/');
console.log(url);
// Current output: https://rollupjs.org/guide%2Fen%2F
// Expected output: https://rollupjs.org/guide/en/
```

Also noticed that empty strings are handled differently now:
```js
const url = getRollupUrl('');
console.log(url);
// Current output: https://rollupjs.org
// Expected output: https://rollupjs.org/
```

### Expected behavior

The function should preserve the snippet path structure without encoding slashes. URLs should remain valid and navigable to the Rollup documentation.

### System Info
- Version: latest main branch

---
Repository: /testbed
