# Bug Report

### Describe the bug

I'm encountering an issue where modules are not being included in the bundle correctly. It appears that some modules that should be included in the output are being excluded, particularly when dealing with dynamic imports.

### Reproduction

```js
// entry.js
import('./dynamic-module.js');

// dynamic-module.js
export default function() {
  console.log('Dynamic module loaded');
}
```

When building with the above setup, the dynamically imported module is not being included in the bundle even though it's clearly referenced. This seems to affect modules that are only imported dynamically and are not entry points themselves.

### Expected behavior

All modules that are:
- Explicitly marked as entry points
- Included through static imports
- Imported dynamically from other included modules

should be present in the final bundle output.

### Additional context

This might be related to how the bundler determines which modules to include. The issue seems to have appeared recently and is causing runtime errors when the dynamic import tries to load a module that wasn't bundled.

---
Repository: /testbed
