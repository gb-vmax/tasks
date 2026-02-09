# Bug Report

### Describe the bug

I'm experiencing an issue where function parameters with nested properties are not being properly tracked for side effects. It seems like the tree-shaking is being too aggressive and removing code that should actually be kept.

### Reproduction

```js
function processData(config) {
  config.nested.value.method();
  return config;
}

const result = processData({
  nested: {
    value: {
      method: () => console.log('side effect')
    }
  }
});
```

When bundling this code, the function call gets incorrectly tree-shaken even though it has side effects. The method call should be preserved in the output but it's being removed.

### Expected behavior

The bundler should detect that `config.nested.value.method()` has potential side effects and preserve it in the output. Deep property access on function parameters should be tracked correctly to determine if code can be safely removed.

### Additional context

This seems to affect scenarios where:
1. Function parameters are accessed through multiple levels of nesting
2. Methods are called on deeply nested properties
3. The parameter object has a complex structure

The code was working correctly before but now these legitimate side effects are being eliminated during the build process.

---
Repository: /testbed
