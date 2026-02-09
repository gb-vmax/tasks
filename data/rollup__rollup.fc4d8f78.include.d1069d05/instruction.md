# Bug Report

### Describe the bug

I'm experiencing an issue with tree-shaking where member expressions are being incorrectly included or excluded from the bundle. It seems like the logic for determining when to include member expression nodes and their associated variables has been inverted somehow.

### Reproduction

```js
// index.js
import { obj } from './module.js';

console.log(obj.property);

// module.js
export const obj = {
  property: 'value',
  unusedProperty: 'should be tree-shaken'
};
```

When bundling this code, I'm seeing unexpected behavior where:
1. Either properties that should be included are being excluded from the bundle
2. Or properties that should be tree-shaken are being kept in the bundle

The behavior seems inconsistent with how member expression inclusion should work - it appears the conditions for when to include nodes and traverse variable paths have been flipped.

### Expected behavior

Member expressions should be properly included in the bundle when they're actually used, and the tree-shaking should correctly identify and remove unused properties. The inclusion logic should properly handle both the case where children are recursively included and when they're not.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
