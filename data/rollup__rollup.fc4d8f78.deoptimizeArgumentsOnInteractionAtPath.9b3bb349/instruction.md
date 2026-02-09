# Bug Report

### Describe the bug

I'm experiencing an issue with conditional expressions where the alternate branch seems to be getting deoptimized too aggressively. When using ternary operators with object property access, the bundler is not properly tracking paths through the alternate (false) branch, which causes unexpected behavior in the output code.

### Reproduction

```js
const obj = {
  foo: {
    bar: 'value'
  }
};

const result = condition ? obj.foo.bar : obj.foo.baz;
```

In this case, when the condition is evaluated, the alternate branch (`obj.foo.baz`) appears to be losing path information. This affects tree-shaking and optimization decisions for the alternate branch.

### Expected behavior

Both the consequent and alternate branches of a conditional expression should maintain proper path tracking. The alternate branch should preserve the same path information as the consequent branch for accurate deoptimization analysis.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
