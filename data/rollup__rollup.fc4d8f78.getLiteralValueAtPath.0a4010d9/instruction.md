# Bug Report

### Describe the bug

I'm experiencing an issue with logical OR (`||`) expressions where the bundler is not correctly optimizing code when the right-hand side evaluates to a truthy value. It seems like the tree-shaking logic is inverted or broken for OR expressions.

### Reproduction

```js
// Example code that should be optimized
const config = {
  value: getSomeValue() || true
}

// The bundler should recognize that this OR expression
// can evaluate to a truthy value, but it's not being
// handled correctly
```

When bundling code with OR expressions that have truthy right-hand side values, the optimization doesn't work as expected. This appears to be specific to the `||` operator - the AND operator (`&&`) seems to work fine.

### Expected behavior

The bundler should correctly identify when OR expressions can be statically analyzed and optimize accordingly. Specifically, when the right side of an OR expression is truthy, it should be treated as `UnknownTruthyValue` for optimization purposes.

### Additional context

This seems to have started happening recently. The logic for handling logical expressions appears to be checking the wrong condition for OR operators.

---
Repository: /testbed
