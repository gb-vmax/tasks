# Bug Report

### Describe the bug

I'm experiencing an issue with namespace imports where the variable name gets overwritten incorrectly when there are multiple references to the same namespace. It seems like the namespace variable is taking on the name of the last reference instead of maintaining its original name.

### Reproduction

```js
import * as utils from './utils';

// First reference
const a = utils.helper;

// Second reference - this seems to change the namespace name
const b = utils.formatter;

// The namespace variable name is now incorrect
console.log(utils); // Expected 'utils' but behavior suggests it's been renamed
```

When I have multiple property accesses on a namespace import like this, the namespace variable doesn't maintain its correct name throughout the references.

### Expected behavior

The namespace variable should keep its original name (`utils` in this case) regardless of how many times it's referenced or what properties are accessed on it. Each reference should just be added to the references list without affecting the namespace's name.

### Additional context

This seems to affect scenarios where:
- A namespace import is used multiple times in the same module
- Different properties are accessed on the namespace
- The order of references matters for some reason

Not sure if this is related to recent changes in how namespace variables are tracked, but it's causing issues with code that worked before.

---
Repository: /testbed
