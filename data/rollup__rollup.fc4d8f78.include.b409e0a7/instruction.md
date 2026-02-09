# Bug Report

### Describe the bug

I'm encountering an issue with member expression evaluation where properties are being included in the bundle even when they shouldn't be. It seems like the tree-shaking logic isn't working correctly for deeply accessed properties.

### Reproduction

```js
// module.js
export const obj = {
  used: {
    prop: 'value'
  },
  unused: {
    prop: 'should be removed'
  }
};

// main.js
import { obj } from './module.js';
console.log(obj.used.prop);
```

When bundling this code, the `unused` property and its nested content are still being included in the final output even though they're never referenced. This is causing unnecessary bloat in the bundle.

### Expected behavior

Only `obj.used.prop` should be included in the bundle. The `unused` branch should be tree-shaken out completely since it's never accessed in the code.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started recently, not sure if it's related to any recent changes in how member expressions are handled during the inclusion phase.

---
Repository: /testbed
