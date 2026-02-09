# Bug Report

### Describe the bug

The `isNotNullOrUndefined` utility function is returning incorrect results. It's supposed to filter out null and undefined values, but it's now returning `true` even when values are null or undefined.

### Reproduction

```js
import { isNotNullOrUndefined } from './common/misc';

const testValue = null;
console.log(isNotNullOrUndefined(testValue)); // Expected: false, Actual: true

const undefinedValue = undefined;
console.log(isNotNullOrUndefined(undefinedValue)); // Expected: false, Actual: true

const validValue = "test";
console.log(isNotNullOrUndefined(validValue)); // Expected: true, Actual: true
```

This is breaking array filtering operations where we need to remove null/undefined values:

```js
const array = [1, null, 2, undefined, 3];
const filtered = array.filter(isNotNullOrUndefined);
console.log(filtered); // Expected: [1, 2, 3], Actual: [1, null, 2, undefined, 3]
```

### Expected behavior

The function should return `false` when the value is null or undefined, and `true` for all other values. This is critical for type narrowing in TypeScript as well.

---
Repository: /testbed
