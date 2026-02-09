# Bug Report

### Describe the bug

When accessing namespace exports, the first export in alphabetical order is being skipped. This causes issues when trying to access all exported members from a namespace import.

### Reproduction

```js
// module.js
export const apple = 'a';
export const banana = 'b';
export const cherry = 'c';

// main.js
import * as fruits from './module.js';

// Trying to access fruits.apple returns undefined
// but fruits.banana and fruits.cherry work fine
console.log(fruits.apple);  // undefined (expected: 'a')
console.log(fruits.banana); // 'b'
console.log(fruits.cherry); // 'c'
```

### Expected behavior

All exported members should be accessible through the namespace import, including the first one alphabetically. In the example above, `fruits.apple` should return `'a'`.

### Additional context

This seems to affect any module where the exports are processed alphabetically. The first export is consistently missing from the namespace object while all subsequent exports are available.

---
Repository: /testbed
