# Bug Report

### Describe the bug

When using `import.meta.file` or `import.meta.ROLLUP_FILE_URL_*`, the referenced file name is not being resolved correctly. It seems like the meta property check is inverted - it's only working when the meta object is NOT `import`, which doesn't make sense.

### Reproduction

```js
// In a module using import.meta
console.log(import.meta.file);
// Expected: resolves to the correct file name
// Actual: returns null or undefined

// Same issue with ROLLUP_FILE_URL_*
const fileUrl = import.meta.ROLLUP_FILE_URL_someId;
// Expected: resolves to the emitted file URL
// Actual: not working as expected
```

### Expected behavior

`import.meta.file` and `import.meta.ROLLUP_FILE_URL_*` should correctly resolve to their respective file names/URLs. The condition should check if the meta name equals `import`, not if it's NOT equal to `import`.

### System Info
- Rollup version: latest
- Node version: 18.x

This looks like it might have been introduced in a recent change where the condition got flipped accidentally.

---
Repository: /testbed
