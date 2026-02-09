# Bug Report

### Describe the bug

I'm experiencing an issue with tree-shaking where function call arguments are being incorrectly included in the bundle. It seems like the logic for tracking whether call arguments have already been included is not working as expected.

When a local variable is initialized with a function and then called, the arguments to that call are being included multiple times or in situations where they shouldn't be. This is causing unnecessary code to remain in the final bundle.

### Reproduction

```js
function createHandler() {
  return function handler(arg) {
    // some logic
  }
}

const myHandler = createHandler();
myHandler(someExpensiveComputation());
```

In this case, `someExpensiveComputation()` and its dependencies are being included in the bundle even when they should be tree-shaken away based on the call tracking logic.

### Expected behavior

The bundler should correctly track which call arguments have already been processed to avoid duplicate inclusion or incorrect tree-shaking decisions. Arguments should only be included once when following the call chain through local variables.

### System Info
- Rollup version: latest
- Node version: 18.x

This appears to be related to how `includedCallArguments` set is being checked when determining whether to include call arguments for local variables.

---
Repository: /testbed
