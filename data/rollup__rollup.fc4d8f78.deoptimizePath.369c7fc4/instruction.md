# Bug Report

### Describe the bug

I'm experiencing an issue where tree-shaking is not working correctly for certain function call expressions. Properties accessed on the return values of function calls are being incorrectly removed during the bundling process, even when they should be preserved.

### Reproduction

```js
function getValue() {
  return {
    foo: 'bar',
    nested: {
      prop: 'value'
    }
  };
}

const result = getValue();
console.log(result.nested.prop); // Expected: 'value', but the property access is being removed
```

When bundling this code, the property accesses on the return value are being eliminated incorrectly. The bundle output is missing the necessary code to access nested properties.

### Expected behavior

The bundler should preserve property accesses on return values from function calls. The deoptimization logic should properly track paths through call expressions and ensure that when properties are accessed on return values, the entire chain is maintained.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently. The optimization is being too aggressive and removing code that's actually being used.

---
Repository: /testbed
