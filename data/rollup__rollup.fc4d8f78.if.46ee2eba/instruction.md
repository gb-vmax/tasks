# Bug Report

### Describe the bug

When using the `extend` option with IIFE format and named exports, the generated bundle has incorrect behavior. The exports object is not being properly extended from existing global variables.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  output: {
    file: 'dist/bundle.js',
    format: 'iife',
    name: 'MyLib',
    extend: true
  }
}

// src/index.js
export const foo = 'bar';
export const baz = 'qux';
```

After building, the generated IIFE doesn't correctly extend the existing `MyLib` global if it already exists. Instead of merging with the existing object, it seems to create a new empty object.

### Expected behavior

When `extend: true` is set, the bundle should check if the global variable already exists and extend it with new exports, preserving any existing properties. The exports parameter should be added to the function parameters list so that new exports can be properly assigned.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
