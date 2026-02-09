# Bug Report

### Describe the bug

I'm experiencing an issue where side effects from logical expressions are not being properly detected in certain cases. It seems like the bundler is incorrectly tree-shaking code that should be preserved because it has side effects.

### Reproduction

```js
const obj = {
  get value() {
    console.log('side effect!');
    return true;
  }
};

// This should preserve the side effect, but it's being removed
const result = false || obj.value;
```

When bundling this code, the getter access on `obj.value` is being incorrectly optimized away even though it has a side effect (the console.log). The final bundle doesn't include the property access at all.

### Expected behavior

The bundler should detect that accessing `obj.value` has side effects and preserve it in the output. Both branches of a logical expression should be checked for side effects when the used branch cannot be determined statically.

### Additional context

This appears to affect logical OR (`||`) and AND (`&&`) expressions where one or both operands have side effects. The issue manifests when the bundler tries to determine if the expression can be safely removed during tree-shaking.

---
Repository: /testbed
