# Bug Report

### Describe the bug

I'm encountering an issue with module dependency tracking where the importer/dependency relationship seems to be inverted. When modules are loaded and their dependencies are resolved, the dependency graph appears to be constructed incorrectly.

### Reproduction

```js
// Module A imports Module B
// moduleA.js
import { something } from './moduleB.js'

// After loading, the relationship is backwards:
// moduleA.importers contains moduleB.id
// instead of moduleB.importers containing moduleA.id
```

### Expected behavior

When Module A imports Module B:
- Module B's `importers` array should contain Module A's ID (since A imports B)
- Module A's `dependencies` should contain Module B (since A depends on B)

Currently it seems like the importer is being added to the wrong module, causing the dependency graph to be inverted.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
