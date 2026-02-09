# Bug Report

### Describe the bug

I'm getting incorrect warnings about illegal import reassignment when trying to reassign properties on regular imported objects (not namespaces). The warning is being triggered even though the reassignment should be valid.

### Reproduction

```js
import obj from './module.js';

// This triggers a warning but shouldn't
obj.property = 'new value';
```

The code above shows a warning like "Illegal reassignment to import 'obj'" even though `obj` is just a regular imported object, not a namespace import. The warning should only appear for namespace imports like:

```js
import * as namespace from './module.js';

// This SHOULD warn
namespace.property = 'new value';
```

### Expected behavior

Warnings about illegal import reassignment should only be shown when attempting to reassign properties on namespace imports (`import * as`), not on regular default or named imports.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
