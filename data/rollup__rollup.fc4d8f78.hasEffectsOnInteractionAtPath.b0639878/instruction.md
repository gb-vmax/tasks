# Bug Report

### Describe the bug

I'm experiencing an issue where side effects from property access and method calls are not being properly tracked. Code that should be included in the bundle because it has side effects is being incorrectly tree-shaken away.

### Reproduction

```js
const obj = {
  get value() {
    console.log('Side effect!');
    return 42;
  }
};

// This access has a side effect but gets removed
obj.value;

// Method calls with side effects also get removed
someObject.methodWithSideEffect();
```

After bundling, these expressions are completely removed from the output even though they have observable side effects (like logging, modifying global state, etc.).

### Expected behavior

Expressions with side effects should be preserved in the bundle. Property access and method calls that can potentially cause side effects should not be tree-shaken away.

### Additional context

This seems to have started happening recently. Previously, the bundler was more conservative about removing code that could have side effects. Now it's being too aggressive with tree-shaking and removing code that actually needs to run.

---
Repository: /testbed
