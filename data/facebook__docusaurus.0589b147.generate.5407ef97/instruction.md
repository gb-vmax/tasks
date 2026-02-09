# Bug Report

### Describe the bug

The `generate` function is returning the wrong value after processing. Instead of returning the generated output string, it's returning the generator object itself. This causes any code that depends on the output to fail or behave unexpectedly.

### Reproduction

```js
const result = generate(myNode, options);
// result should be a string with the generated output
// but instead it's returning the generator object
console.log(typeof result); // Expected: 'string', Actual: 'object'
```

When trying to use the generated code, I'm getting errors because the return value is not what's expected. The function used to return `state.output` which contained the actual generated code, but now it's returning something else entirely.

### Expected behavior

The `generate` function should return the generated output string that was built up during the processing of the node tree. Any code that calls `generate()` should receive a usable string output, not an internal object.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
