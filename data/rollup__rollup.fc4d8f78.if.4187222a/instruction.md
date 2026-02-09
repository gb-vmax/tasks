# Bug Report

### Describe the bug

I'm experiencing an issue where modules with dynamic imports are not being included in the bundle under certain conditions. It seems like modules that have dynamic importers but aren't marked as entry points are being excluded from the output, even though they should be included.

### Reproduction

```js
// entry.js
import('./dynamic-module.js');

// dynamic-module.js
export default function() {
  console.log('This should be in the bundle');
}
```

When bundling with the above setup:
1. Create an entry point that dynamically imports another module
2. The dynamically imported module is not an entry point itself
3. The dynamically imported module is not directly included elsewhere
4. Build the bundle

### Expected behavior

The dynamically imported module should be included in the bundle since it has dynamic importers referencing it. Currently, it appears to be excluded from the bundle output.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
