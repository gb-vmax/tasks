# Bug Report

### Describe the bug

I'm encountering a syntax error when trying to use the library. It seems like there's an issue with the module exports in the `estree-util-value-to-estree` vendor file. The code is trying to execute what looks like function implementation code directly in the export statement, which is causing parsing errors.

### Reproduction

```js
// Simply importing the module causes an error
import { valueToEstree } from './jest/vendor/estree-util-value-to-estree@3.0.1.js';

// The module fails to load with a syntax error
```

### Expected behavior

The module should export the `valueToEstree` function properly and be importable without errors. The export statement should reference the function, not contain the implementation inline.

### Additional context

This appears to have broken after a recent update. The export block seems malformed - it looks like function implementation code was accidentally placed where only export declarations should be. The file structure doesn't match standard JavaScript module syntax.

---
Repository: /testbed
