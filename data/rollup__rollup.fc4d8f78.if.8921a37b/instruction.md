# Bug Report

### Describe the bug

I'm experiencing an issue with dynamic imports where modules that should be treated as dynamic entry points are not being properly detected. It seems like the logic for identifying dynamic entry modules has inverted behavior - modules are only being added when they're already in the entries set, rather than when they're not.

### Reproduction

```js
// Entry module
import('./dynamic-module.js');

// dynamic-module.js contains:
export default function() {
  console.log('Dynamic module loaded');
}
```

When bundling with dynamic imports, the dynamic module is not being properly identified as a dynamic entry point. This causes issues with chunk generation where the dynamically imported module doesn't get its own chunk as expected.

### Expected behavior

Dynamic imports should be properly identified and added to the dynamic entry modules set when they:
1. Are Module instances
2. Have included dynamic importers
3. Are NOT already in the all entries set

The awaited dynamic imports detection also seems inverted - it's checking for modules that are NOT in static dependencies when it should be checking for modules that ARE in static dependencies.

### System Info
- Rollup version: latest
- Node version: 18.x

This is causing incorrect chunk assignment in my build output. The dynamic imports are either being bundled into the wrong chunks or not being split properly.

---
Repository: /testbed
