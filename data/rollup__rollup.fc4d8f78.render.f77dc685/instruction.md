# Bug Report

### Describe the bug

When bundling code that contains object expressions with properties, the output is getting corrupted. Objects with properties are being completely removed from the bundle, leaving only empty object literals `{}`.

### Reproduction

```js
// Input code
const config = {
  name: 'my-app',
  version: '1.0.0',
  settings: {
    debug: true
  }
};

export default config;
```

After bundling, the output becomes:

```js
const config = {};

export default config;
```

All the properties are stripped out even though they should be included in the final bundle.

### Steps to reproduce
1. Create a module that exports an object with properties
2. Bundle the code
3. Check the output - the object will be empty

### Expected behavior

The object should retain all its properties in the bundled output. Empty objects `{}` should remain empty, but objects with properties should keep those properties.

### Additional context

This seems to affect any object literal that has at least one property. Empty objects work fine, but as soon as you add properties, they get removed during the bundling process.

---
Repository: /testbed
