# Bug Report

### Describe the bug

I'm experiencing an issue with interop helpers when bundling modules with multiple dependencies that require different interop helpers. It seems like the interop helper tracking is getting cleared prematurely, causing only the last helper to be registered instead of accumulating all needed helpers.

### Reproduction

When bundling a module that imports multiple dependencies requiring interop helpers (e.g., default imports from CommonJS modules), only one helper gets tracked:

```js
// Module with multiple imports requiring interop
import foo from 'commonjs-module-1';
import bar from 'commonjs-module-2';
import baz from 'commonjs-module-3';

console.log(foo, bar, baz);
```

After bundling, the `neededInteropHelpers` set appears to only contain one helper instead of tracking all the helpers that were added during the process.

### Expected behavior

All interop helpers that are needed for the bundle should be tracked and included in the output. The `neededInteropHelpers` set should accumulate helpers as they're added, not lose them after each addition.

### Additional context

This appears to affect scenarios where multiple modules require the same or different interop helpers. The helper registration mechanism seems to be interfering with the tracking of which helpers are actually needed for the final output.

---
Repository: /testbed
