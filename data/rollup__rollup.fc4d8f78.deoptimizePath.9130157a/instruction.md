# Bug Report

### Describe the bug

I'm experiencing an issue where tree-shaking is not working correctly for certain call expressions. It seems like properties accessed on function return values are being incorrectly retained in the bundle even when they should be eliminated as dead code.

### Reproduction

```js
function getData() {
  return {
    used: 'this should be kept',
    unused: 'this should be removed'
  };
}

const result = getData();
console.log(result.used);
// The 'unused' property is still appearing in the output bundle
```

When bundling this code, both `used` and `unused` properties are included in the final output, but only `used` is actually referenced. The `unused` property should be tree-shaken away.

### Expected behavior

Only the `used` property should appear in the bundled output. Unused properties from function return values should be eliminated during the tree-shaking optimization pass.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started recently, possibly related to deoptimization tracking changes. The bundler appears to be too conservative in what it keeps.

---
Repository: /testbed
