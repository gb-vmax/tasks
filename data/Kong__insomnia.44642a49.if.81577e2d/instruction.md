# Bug Report

### Describe the bug

The `isNotNullOrUndefined` function is behaving unexpectedly - it seems to always return `true` regardless of the input value. I'm passing in `null` and `undefined` values but they're not being filtered out as expected.

### Reproduction

```js
import { isNotNullOrUndefined } from './common/misc';

const values = [null, undefined, 'test', 0, false];
const filtered = values.filter(isNotNullOrUndefined);

console.log(filtered);
// Expected: ['test', 0, false]
// Actual: [null, undefined, 'test', 0, false]
```

The function appears to not be filtering anything out. Even when I try using the new options parameter:

```js
const values = ['', [], {}, NaN, 'valid'];
const filtered = values.filter(v => isNotNullOrUndefined(v, { 
  filterEmptyStrings: true,
  filterEmptyArrays: true,
  filterEmptyObjects: true,
  filterNaN: true
}));

console.log(filtered);
// Expected: ['valid']
// Actual: ['', [], {}, NaN, 'valid']
```

### Expected behavior

The function should return `false` for `null` and `undefined` values, and when options are provided, it should also filter out empty strings, empty arrays, empty objects, and NaN values accordingly.

### System Info
- Insomnia version: latest
- Node version: 18.x

---
Repository: /testbed
