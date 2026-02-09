# Bug Report

### Describe the bug

When using logical expressions (`&&`, `||`, `??`) with function calls, the purity tracking seems to be incorrect. The bundler is not properly determining whether the resulting expression is pure or has side effects, which can lead to incorrect tree-shaking or optimization behavior.

### Reproduction

```js
const obj1 = {
  method() {
    console.log('side effect');
    return 42;
  }
};

const obj2 = {
  method() {
    return 100;
  }
};

// Using logical expression with method calls
const result = (condition && obj1 || obj2).method();
```

In this case, when the logical expression's branches can't be statically determined, the purity of the overall expression should reflect whether any of the branches have side effects. However, it appears the purity information is not being properly propagated through both branches of the logical expression.

### Expected behavior

The bundler should correctly track whether expressions involving logical operators have side effects by checking all possible branches. If either branch of a logical expression has side effects, the entire expression should be marked as impure.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
