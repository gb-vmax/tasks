# Bug Report

### Describe the bug

I'm experiencing an issue with logical expressions where the wrong branch is being included in the bundle. When using logical operators like `&&` or `||`, it seems like the tree-shaking logic is incorrectly determining which side of the expression should be included.

### Reproduction

```js
const config = {
  feature: true
};

// Using logical AND
const result = config.feature && expensiveFunction();

function expensiveFunction() {
  console.log('This should be included');
  return { data: 'value' };
}
```

In this case, when the left side of the `&&` expression is used, the right side (expensiveFunction) is not being included in the bundle even though it should be, resulting in runtime errors.

### Expected behavior

Both branches of a logical expression should be properly included when needed. If the left side of an AND expression is the used branch and the right side should be included based on the context, then both sides need to be in the final bundle.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
