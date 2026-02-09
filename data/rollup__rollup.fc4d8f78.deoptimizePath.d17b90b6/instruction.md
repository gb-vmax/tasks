# Bug Report

### Describe the bug

I'm experiencing an issue where namespace imports are incorrectly allowed to be reassigned in certain scenarios. When accessing a nested property on a namespace import (like `namespace.prop.nested`), the reassignment check doesn't trigger properly and allows invalid code to pass through without warnings.

### Reproduction

```js
import * as myNamespace from './module';

// This should trigger an error but doesn't
myNamespace.something.value = 'new value';
```

The issue seems to occur specifically when there's a nested property access (more than one level deep) on the namespace object. Direct property assignment like `myNamespace.something = value` works correctly and triggers the appropriate error, but accessing deeper properties bypasses the check.

### Expected behavior

Any attempt to reassign properties on a namespace import, regardless of nesting level, should be detected and flagged appropriately. The behavior should be consistent whether you're accessing `namespace.prop` or `namespace.prop.nested`.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
