# Bug Report

### Describe the bug

I'm experiencing an issue with function parameter tracking when calling methods on objects passed as parameters. It seems like the deoptimization logic for nested property access isn't working correctly anymore.

When a parameter object has a method called on one of its properties (like `param.someProperty.method()`), the deoptimization doesn't happen as expected. This causes incorrect tree-shaking behavior where code that should be retained gets removed.

### Reproduction

```js
function processData(config) {
  // Calling a method on a nested property
  config.handler.process();
  return config.value;
}

const myConfig = {
  handler: {
    process: () => {
      console.log('Processing...');
      sideEffect();
    }
  },
  value: 42
};

processData(myConfig);
```

In this case, the `sideEffect()` call inside `handler.process()` is being incorrectly removed during bundling, even though it has observable side effects.

### Expected behavior

When a method is called on a nested property of a parameter object, the bundler should properly deoptimize and retain any side effects within that call chain. The `handler.process()` method and its contents should not be tree-shaken away.

### Additional context

This seems to affect scenarios where:
- Parameter objects have nested properties
- Methods are called on those nested properties
- The logic for tracking which paths have been deoptimized may be inverted or checking the wrong condition

---
Repository: /testbed
