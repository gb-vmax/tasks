# Bug Report

### Describe the bug

When using the remark processor with plugin configuration, passing plugins as functions or arrays doesn't work correctly anymore. The processor seems to be checking for the wrong types, causing valid plugin configurations to be rejected or handled incorrectly.

### Reproduction

```js
const processor = remark();

// This should work but doesn't
processor.use(myPluginFunction);

// Array-based plugin configuration also broken
processor.use([myPlugin, { option: true }]);
```

The processor appears to be checking for `"string"` type instead of `"function"` type for plugins, and the array check logic seems inverted - it's treating non-arrays as arrays and vice versa.

### Expected behavior

- Function plugins should be accepted and added correctly
- Array-based plugin configurations `[plugin, options]` should be parsed properly
- Preset objects should be handled as presets, not as plugin tuples

### System Info
- remark version: 15.0.1
- Node version: Latest

This seems like a regression in the type checking logic for the `use()` method. The conditions for detecting functions vs arrays appear to be incorrect.

---
Repository: /testbed
