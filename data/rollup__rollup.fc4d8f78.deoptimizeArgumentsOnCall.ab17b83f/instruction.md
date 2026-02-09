# Bug Report

### Describe the bug

I'm experiencing an issue with `CustomEvent` objects where the `detail` property is not being properly tracked for optimization. When creating a CustomEvent with a detail object, modifications to the detail property seem to be optimized away incorrectly.

### Reproduction

```js
const event = new CustomEvent('myEvent', {
  detail: {
    value: 'test'
  }
});

// Access to detail property seems to be incorrectly optimized
console.log(event.detail.value);
```

### Expected behavior

The `detail` property of CustomEvent should be properly deoptimized and its nested properties should be accessible. The bundler should not incorrectly optimize away access to `event.detail` and its properties.

### Additional context

This appears to affect how CustomEvent constructor arguments are analyzed during the optimization phase. The detail object passed in the second argument (the options object) should be treated carefully to avoid incorrect tree-shaking.

---
Repository: /testbed
