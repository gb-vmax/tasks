# Bug Report

### Describe the bug

After updating to the latest version, modules that should be included in the bundle are being unexpectedly tree-shaken out. This is causing runtime errors when trying to access code that was previously bundled correctly.

### Reproduction

```js
// module.js
export function sideEffect() {
  window.globalState = { initialized: true };
}

// main.js
import './module.js';

console.log(window.globalState); // undefined - module was tree-shaken
```

The module `module.js` has side effects (modifying global state) but is being removed from the bundle entirely. This worked fine in previous versions.

### Expected behavior

Modules with side effects should be included in the bundle by default, even if their exports aren't explicitly used. The `moduleSideEffects` option should preserve modules that perform initialization or other side-effecting operations.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
