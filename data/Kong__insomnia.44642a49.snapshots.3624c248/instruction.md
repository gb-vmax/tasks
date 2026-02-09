# Bug Report

### Describe the bug

The `branchSchema` has a syntax error that breaks the schema definition. When trying to use the branch schema, it fails to compile/parse correctly due to malformed structure.

### Reproduction

```js
import { branchSchema } from './type-schemas';

// Attempting to use the schema fails
const branch = createBuilder(branchSchema).build();
```

The schema definition for `Branch` appears to have code placed outside of the object structure. There are function declarations (`generateSnapshots` and `generateBlobId`) that are defined in the middle of the schema object, breaking the valid JavaScript object syntax.

### Expected behavior

The `branchSchema` should be a valid schema object that can be used to create branch instances. The schema should properly define default values for all properties including `snapshots`.

### Additional context

Looking at the schema definition, it seems like helper functions were added but not properly structured within the object. The `snapshots` property definition is also split across multiple locations which causes parsing issues.

---
Repository: /testbed
