# Bug Report

### Describe the bug

I'm experiencing an issue with function parameter handling in tree-shaking. When a function uses destructuring parameters or rest parameters along with the `arguments` object, the parameters are not being included in the output bundle as expected.

### Reproduction

```js
function example({ a, b }, ...rest) {
  console.log(arguments);
  return a + b;
}

export { example };
```

After bundling, the destructured parameters `{ a, b }` and rest parameter `...rest` are missing from the output even though they should be included since the function references the `arguments` object.

### Expected behavior

When a function uses the `arguments` object, all parameters (including destructuring patterns and rest parameters) should be preserved in the bundled output, since they affect the `arguments` object's behavior.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
