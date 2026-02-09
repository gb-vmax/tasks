# Bug Report

### Describe the bug

Dynamic imports are being incorrectly tree-shaken and removed from the bundle even when they should be preserved. This causes runtime errors when the application tries to execute code that relies on these dynamic imports.

### Reproduction

```js
// Module: lazy-loader.js
export async function loadModule() {
  const module = await import('./heavy-module.js');
  return module.default;
}

// Main entry
import { loadModule } from './lazy-loader.js';

// This call fails at runtime because the import was removed
loadModule().then(result => console.log(result));
```

When bundling this code, the dynamic `import()` statement gets removed during tree-shaking, causing the `loadModule()` function to fail at runtime with an error about missing modules.

### Expected behavior

Dynamic imports should always be preserved in the bundle since they have side effects and are evaluated at runtime. The bundler should treat `import()` expressions as having effects to prevent them from being removed during dead code elimination.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems like a regression as dynamic imports were working correctly in previous builds. The issue appears to be related to how side effects are tracked for import expressions.

---
Repository: /testbed
