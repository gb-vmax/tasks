# Bug Report

### Describe the bug
When using the `system` output format with a single named export, the generated code has the export name and value arguments swapped in the `exports()` call. This causes the exported binding to have the wrong name at runtime.

### Reproduction
```js
// rollup.config.js
export default {
  input: 'src/index.js',
  output: {
    format: 'system',
    file: 'dist/bundle.js'
  }
}

// src/index.js
export const myValue = 42;
```

After bundling, the generated SystemJS code calls `exports()` with the arguments in the wrong order - it passes the value first and the name second, when it should be name first, then value.

### Expected behavior
The `exports()` function should be called with the export name as the first argument and the export value as the second argument, like:
```js
exports("myValue", myValue);
```

Instead it's generating:
```js
exports(myValue, "myValue");
```

This breaks the module when loaded in a SystemJS environment because the export gets registered with the wrong key.

### System Info
- Rollup version: latest
- Output format: system

---
Repository: /testbed
