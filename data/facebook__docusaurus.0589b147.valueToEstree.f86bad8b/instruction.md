# Bug Report

### Describe the bug

The `valueToEstree` function is not being exported correctly from the module. When trying to import and use it, I'm getting an error that the function is undefined or not accessible.

### Reproduction

```js
import { valueToEstree } from 'estree-util-value-to-estree';

const result = valueToEstree(42);
// Error: valueToEstree is not a function or is undefined
```

### Expected behavior

The function should be properly exported and accessible when imported. It should convert JavaScript values to ESTree AST nodes as documented.

### System Info
- Node version: 18.x
- Package version: 3.0.1

This seems to have broken after a recent update. The export statement appears to be malformed or incomplete in the module file.

---
Repository: /testbed
