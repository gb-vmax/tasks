# Bug Report

### Describe the bug

I'm encountering an issue with dynamic import expressions that have invalid import attributes/assertions. When an import expression includes options that are not an object literal (e.g., a variable or other expression), the warning message is no longer being displayed as expected.

### Reproduction

```js
// This should trigger a warning but doesn't anymore
const opts = { assert: { type: 'json' } };
import('./data.json', opts);

// Or with any non-object-literal expression
import('./module.js', someVariable);
```

### Expected behavior

A warning should be logged when import attributes are provided but are not valid object literals. Previously, these cases would trigger a warning message indicating that the import attribute is invalid, but now the warning is only shown when options are completely absent.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
