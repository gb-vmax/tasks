# Bug Report

### Issue with `nodeTypes` export returning unexpected values

I'm experiencing an issue with the `nodeTypes` export from `@mdx-js/mdx` where it's returning a copy of the object/array instead of the original reference. This is causing problems when trying to check identity or modify the nodeTypes.

### Reproduction
```js
import { nodeTypes } from '@mdx-js/mdx';

// Get nodeTypes twice
const types1 = nodeTypes;
const types2 = nodeTypes;

// These should be the same reference but they're not
console.log(types1 === types2); // Expected: true, Actual: false
```

Every time I access `nodeTypes`, I get a new copy instead of the same reference. This breaks code that relies on reference equality or tries to modify the nodeTypes object.

### Expected behavior
The `nodeTypes` export should return the same reference each time it's accessed, not create a new copy with spread operators.

### Additional context
This seems to have changed recently. Previously, accessing `nodeTypes` multiple times would return the same object reference, which is the standard behavior for module exports.

---
Repository: /testbed
