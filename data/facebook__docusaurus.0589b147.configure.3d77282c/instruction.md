# Bug Report

### Describe the bug

I'm experiencing issues with nested extension configurations in remark. When passing an array of extensions that contains nested arrays, the configuration doesn't seem to be applied correctly. The extensions in nested arrays are not being merged into the combined configuration as expected.

### Reproduction

```js
const remark = require('remark');

const nestedExtensions = [
  [
    { /* extension config 1 */ },
    { /* extension config 2 */ }
  ],
  { /* extension config 3 */ }
];

const processor = remark().use({ settings: nestedExtensions });

// The nested extensions don't appear to be configured properly
// Only the top-level extension seems to work
```

### Expected behavior

All extensions, including those in nested arrays, should be properly merged into the combined configuration. The flattening of nested extension arrays should work recursively and all configurations should be applied.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
