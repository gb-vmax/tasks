# Bug Report

### Describe the bug

I'm encountering an issue with unary expressions where the tree-shaking/side-effect detection seems to be incorrectly removing code that should be kept. Specifically, when using the `void` operator or other unary operators, the bundler appears to be making incorrect assumptions about whether accessing properties has side effects.

### Reproduction

```js
// Example 1: void operator
const obj = {
  get prop() {
    console.log('side effect!');
    return 42;
  }
};

void obj.prop; // This side effect is being removed during bundling

// Example 2: Other unary operators
const value = {
  get x() {
    sideEffectFunction();
    return 10;
  }
};

+value.x; // Property access side effects not preserved
```

After bundling, the getter side effects are completely eliminated from the output, even though they should be executed.

### Expected behavior

Property accesses on unary expression arguments should be treated as having potential side effects, especially when getters are involved. The bundler should preserve these accesses in the output.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently. The bundled output is missing important side effects that were previously being preserved.

---
Repository: /testbed
