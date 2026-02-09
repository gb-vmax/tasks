# Bug Report

### Describe the bug

I'm experiencing an issue where `import.meta` properties are not being processed correctly in my bundle. It seems like the bundler is not recognizing `import.meta` references properly, which causes the build output to be incorrect.

### Reproduction

```js
// Input code
console.log(import.meta.url);
console.log(import.meta.resolve('./module.js'));

// After bundling, these import.meta references are not handled as expected
```

When I bundle code that uses `import.meta.url` or other `import.meta` properties, they don't get transformed or included in the output correctly. The resulting bundle either has missing references or doesn't work at runtime.

### Expected behavior

The bundler should properly detect and process `import.meta` expressions, transforming them according to the output format and ensuring they work correctly in the bundled code.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: Linux

---
Repository: /testbed
