# Bug Report

### Describe the bug
When a module imports multiple dependencies, only the first dependency is being added to the module's dependency set. All subsequent dependencies are being tracked as importers but are not properly registered in the module's dependencies collection.

### Reproduction
```js
// moduleA.js
import { foo } from './dep1.js'
import { bar } from './dep2.js'
import { baz } from './dep3.js'

export { foo, bar, baz }
```

When bundling a module with multiple static imports like the above, the module loader only registers the first dependency (`dep1.js`) in the module's dependencies, while `dep2.js` and `dep3.js` are not included even though they should be.

### Expected behavior
All imported dependencies should be added to the module's dependency set, not just the first one. The module should maintain a complete list of its dependencies for proper tree-shaking and bundling.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to affect any module with more than one import statement. The dependency graph becomes incomplete which could lead to incorrect bundling behavior.

---
Repository: /testbed
