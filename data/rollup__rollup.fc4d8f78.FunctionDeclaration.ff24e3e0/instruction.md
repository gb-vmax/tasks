# Bug Report

### Describe the bug

I'm encountering a crash when trying to bundle code that contains anonymous function declarations (specifically `export default function`). The bundler throws an error when processing these declarations, which worked fine in previous versions.

### Reproduction

```js
// This causes an error during bundling
export default function() {
  return 'test';
}
```

The error occurs when Rollup tries to process the anonymous function declaration. It seems like the code is attempting to access properties on a null/undefined identifier.

### Expected behavior

Anonymous function declarations (especially when used with `export default`) should be handled correctly without throwing errors. This is valid JavaScript syntax and should bundle successfully.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to be a regression - the same code bundled without issues before. Any help would be appreciated!

---
Repository: /testbed
