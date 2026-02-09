# Bug Report

### Describe the bug

The `number` property type is not behaving as expected. Instead of returning a simple numeric constant/value, it appears to be returning a function or something that changes state over time. This is causing issues when trying to use numeric property types in my MDX components.

### Reproduction

```js
import { number } from '@mdx-js/mdx';

// Expecting a constant value or simple type identifier
console.log(number); // Returns something unexpected
console.log(typeof number); // Should be a number or constant, but isn't

// When used in property definitions
const props = {
  type: number
};
// Behavior is inconsistent across multiple accesses
```

### Expected behavior

The `number` export should be a simple constant value (like other property types such as `booleanish`, `commaSeparated`, etc.) that can be used to define numeric property types in MDX. It shouldn't be stateful or change between accesses.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
