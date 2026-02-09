# Bug Report

### Describe the bug

I'm experiencing an issue with export shim generation in my bundled output. After bundling, the export shim seems to be toggling on and off unpredictably instead of being set correctly. This is causing inconsistent behavior in the generated code.

### Reproduction

```js
// module.js
export const value = 42;

// When this module is processed and includePath is called multiple times,
// the export shim state flips between enabled and disabled
```

The issue appears when a module's export path is included multiple times during the bundling process. Instead of the export shim being consistently enabled, it seems to alternate states.

### Expected behavior

Once `includePath` is called on an export, the export shim should be set to `true` and remain `true`. It shouldn't toggle or flip-flop between states on subsequent calls.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
