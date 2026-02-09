# Bug Report

### Describe the bug

When using the `extend: true` option with IIFE output format, the exports parameter is not being passed correctly to the function. The generated code seems to be missing the `exports` parameter in the function signature, which causes the bundle to fail at runtime.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  output: {
    file: 'dist/bundle.js',
    format: 'iife',
    name: 'MyLibrary',
    extend: true
  }
}
```

```js
// src/index.js
export const foo = 'bar';
export default function() {
  return 'hello';
}
```

After building, the generated IIFE doesn't properly handle the exports parameter when `extend: true` is set. The exports object is added to the dependencies array but not to the parameters list, resulting in a mismatch between the dependency injection and function parameters.

### Expected behavior

When `extend: true` is used, the IIFE should properly receive and use the exports parameter so that the module can extend an existing global object. Both the dependency array and the function parameters should be in sync.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
