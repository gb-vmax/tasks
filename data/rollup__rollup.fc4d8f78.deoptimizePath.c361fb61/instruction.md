# Bug Report

### Describe the bug

I'm experiencing an issue with namespace imports where reassignment detection seems to be triggering incorrectly. When accessing nested properties on namespace imports, I'm getting unexpected errors about namespace reassignment even though I'm only accessing deep properties, not reassigning the namespace itself.

### Reproduction

```js
import * as myNamespace from './module';

// This triggers an error about namespace reassignment
// even though we're just accessing a nested property
const value = myNamespace.obj.nested.property;
```

The error occurs when trying to access properties that are more than one level deep on a namespace import. It seems like the code is treating deep property access as if it were a namespace reassignment.

### Expected behavior

Accessing nested properties on namespace imports should work without triggering namespace reassignment errors. Only actual reassignments like `myNamespace = something` should be flagged.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
