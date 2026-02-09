# Bug Report

### Describe the bug

I'm experiencing an issue with code generation where options passed to the `generate()` function are not being respected. The generated output doesn't reflect the configuration I'm providing, and it seems like the options are being ignored completely during the generation process.

### Reproduction

```js
const options = {
  indent: 4,
  lineWidth: 80,
  // ... other custom options
};

const result = generate(myNode, options);
// The output doesn't use the specified indent or lineWidth
// It's as if default options are being used instead
```

### Expected behavior

The `generate()` function should use the provided options throughout the entire generation process. Custom indentation, line width, and other configuration should be applied to the generated output.

### Additional context

This appears to have started recently. The options work fine when passed initially, but somewhere in the generation pipeline they seem to get lost or reset to defaults.

---
Repository: /testbed
