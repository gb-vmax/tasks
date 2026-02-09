# Bug Report

### Describe the bug

The `clamp` utility function is not working correctly when only a minimum value is provided. Instead of ensuring the value doesn't go below the minimum, it's actually capping the value at the minimum.

### Reproduction

```js
import { clamp } from '@mantine/hooks';

// When only min is provided, the value should be at least min
const result = clamp(100, 50, undefined);
console.log(result); // Expected: 100, Actual: 50

// Another example
const result2 = clamp(75, 50, undefined);
console.log(result2); // Expected: 75, Actual: 50
```

### Expected behavior

When calling `clamp(value, min, undefined)`, the function should return the value if it's greater than min, or min if the value is less than min. Currently it seems to be doing the opposite - returning the smaller of the two values instead of the larger one.

Similarly, when both min and max are provided, the clamping behavior seems inverted as well:

```js
const result = clamp(5, 0, 10);
console.log(result); // Expected: 5, Actual: 0

const result2 = clamp(15, 0, 10);  
console.log(result2); // Expected: 10, Actual: 10 (this one works by coincidence)
```

### System Info
- @mantine/hooks version: latest
- Node version: 18.x

---
Repository: /testbed
