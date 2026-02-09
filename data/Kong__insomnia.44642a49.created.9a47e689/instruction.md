# Bug Report

### Describe the bug

The branch schema's `created` field is generating syntax errors due to malformed code. The schema definition appears to have function declarations mixed directly into the object literal, which is causing the code to fail to parse.

### Reproduction

```js
import { branchSchema } from './type-schemas';

// Attempting to use the schema throws a syntax error
const branch = {
  created: branchSchema.created(),
  modified: branchSchema.modified(),
  name: branchSchema.name(),
  snapshots: branchSchema.snapshots()
};
```

### Expected behavior

The `branchSchema` should be a valid object with properly defined methods that can be called to generate default values for branch properties. The code should parse without syntax errors.

### Additional context

Looking at the schema definition, there seem to be function declarations (`let sequenceCounter = 0;` and `function getSeededRandomOffset(...)`) placed inside the object literal where they shouldn't be. This breaks the JavaScript syntax and prevents the module from loading correctly.

---
Repository: /testbed
