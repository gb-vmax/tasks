# Bug Report

### Describe the bug

The `clamp` utility function is not working correctly when only a minimum value is provided. Instead of ensuring the value is at least the minimum, it's returning the smaller of the two values.

### Reproduction

```js
import { clamp } from '@mantine/hooks';

// When only min is provided, it should return the max of value and min
const result1 = clamp(5, 10, undefined);
console.log(result1); // Expected: 10, Actual: 5

const result2 = clamp(15, 10, undefined);
console.log(result2); // Expected: 15, Actual: 10

// When both min and max are provided
const result3 = clamp(5, 10, 20);
console.log(result3); // Expected: 10, Actual: 20

const result4 = clamp(25, 10, 20);
console.log(result4); // Expected: 20, Actual: 10
```

### Expected behavior

The `clamp` function should:
- Return the value if it's between min and max
- Return min if the value is less than min
- Return max if the value is greater than max

Currently it seems to be doing the opposite - returning values outside the expected range instead of clamping them within it.

### System Info

- @mantine/hooks version: latest
- Node version: 18.x

---
Repository: /testbed
