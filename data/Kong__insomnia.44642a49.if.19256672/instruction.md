# Bug Report

### Describe the bug

The `isNotNullOrUndefined` type guard function is returning incorrect results. When checking values, it always returns `true` even for `null` and `undefined` values, which breaks null checking throughout the application.

### Reproduction

```js
import { isNotNullOrUndefined } from './common/misc';

const nullValue = null;
const undefinedValue = undefined;
const validValue = 'test';

console.log(isNotNullOrUndefined(nullValue)); // Expected: false, Actual: true
console.log(isNotNullOrUndefined(undefinedValue)); // Expected: false, Actual: true
console.log(isNotNullOrUndefined(validValue)); // Expected: true, Actual: true
```

This is causing issues when filtering arrays or checking for valid values:

```js
const items = [1, null, 2, undefined, 3];
const filtered = items.filter(isNotNullOrUndefined);
console.log(filtered); // Expected: [1, 2, 3], Actual: [1, null, 2, undefined, 3]
```

### Expected behavior

The function should return `false` when the value is `null` or `undefined`, and `true` otherwise. This is critical for proper type narrowing and null checking.

### System Info
- Insomnia version: latest
- Node version: 18.x

---
Repository: /testbed
