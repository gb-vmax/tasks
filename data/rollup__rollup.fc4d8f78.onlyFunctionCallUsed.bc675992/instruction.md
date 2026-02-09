# Bug Report

### Describe the bug

I'm encountering an issue with function optimization where exported default functions are not being properly recognized. The bundler seems to be treating exported default functions incorrectly, which affects tree-shaking and optimization behavior.

### Reproduction

```js
// module.js
export default function myFunction() {
  console.log('test');
}

// main.js
import myFunction from './module.js';
myFunction();
```

When bundling this code, the function is not being optimized correctly. It seems like the detection logic for how functions are used is getting confused between variable declarations and export default declarations.

### Expected behavior

Exported default functions should be properly analyzed to determine if they're only used as function calls, allowing for correct optimization and tree-shaking.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently, possibly after some refactoring of the function analysis code. The issue specifically affects default exports - named exports and regular variable declarations seem to work fine.

---
Repository: /testbed
