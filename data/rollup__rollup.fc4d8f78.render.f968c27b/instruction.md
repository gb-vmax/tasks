# Bug Report

### Describe the bug

When bundling with `format: 'system'`, exported class declarations are not being handled correctly. The system export statement appears to be generated in the wrong cases, causing exported classes to not be properly registered in the System module format.

### Reproduction

```js
// input.js
export class MyClass {
  constructor() {
    this.value = 42;
  }
}

// rollup.config.js
export default {
  input: 'input.js',
  output: {
    format: 'system',
    file: 'output.js'
  }
}
```

When bundling this code with the System module format, the exported class is not properly registered with the System module loader. The class declaration is present in the output but the export statement that should link it to the System registry is missing or incorrectly placed.

### Expected behavior

The bundled output should include the proper System export registration for the exported class, allowing it to be imported by other System modules. The class should be accessible when the module is loaded in a System-compatible environment.

### System Info
- Rollup version: latest
- Node version: 18.x
- Format: system

---
Repository: /testbed
