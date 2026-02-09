# Bug Report

### Describe the bug

Getting a stack overflow error when using `export default` with certain module configurations. The bundler crashes with a maximum call stack size exceeded error during the build process.

### Reproduction

```js
// module.js
export default class MyClass {
  constructor() {
    this.value = 42;
  }
}

// index.js
import MyClass from './module.js';
const instance = new MyClass();
console.log(instance.value);
```

When bundling these files, the build process hangs and eventually crashes with:

```
RangeError: Maximum call stack size exceeded
```

### Expected behavior

The bundle should complete successfully without any stack overflow errors. The export default statement should be handled correctly and the module should be bundled without infinite recursion.

### System Info
- Node version: 18.x
- OS: macOS

This seems to be related to how export default variables are being tracked internally. The error only happens with certain combinations of imports and exports.

---
Repository: /testbed
