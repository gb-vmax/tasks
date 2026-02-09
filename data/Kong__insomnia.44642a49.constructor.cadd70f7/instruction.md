# Bug Report

### Describe the bug

I'm experiencing an issue where methods on `PropertyBase` objects are suddenly undefined after a recent update. When trying to call methods like `parent()`, `meta()`, `findInParents()`, or `forEachParent()`, I get errors saying these methods don't exist on the object.

### Reproduction

```js
import { PropertyBase } from '@insomnia/sdk';

const property = new PropertyBase('test description');

// These method calls fail with "is not a function" errors
const parentObj = property.parent();
const metaData = property.meta();

// Trying to traverse the parent chain also fails
property.forEachParent({ withRoot: true }, (parent) => {
  console.log(parent);
  return true;
});
```

### Expected behavior

All methods defined on `PropertyBase` should be callable on instances of the class. The object should have access to:
- `parent()` - to get the parent property
- `meta()` - to retrieve metadata
- `forEachParent()` - to iterate through parent chain
- `findInParents()` - to search for properties in parent chain

### System Info

- Package: @insomnia/sdk
- Node version: 18.x

This seems like the class definition might have gotten corrupted or methods were accidentally removed. The PropertyBase class is fundamental to the SDK so this is blocking our workflow.

---
Repository: /testbed
