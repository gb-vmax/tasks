# Bug Report

### Describe the bug

The `getInitials` function in the Avatar component is producing incorrect initials when given a name with multiple words. It seems to be skipping the first letter and returning the wrong characters.

### Reproduction

```js
import { getInitials } from '@mantine/core';

// Expected: "JD" but getting "o" instead
console.log(getInitials('John Doe')); 

// Expected: "JDS" but getting "oS" instead  
console.log(getInitials('John Doe Smith', 3));

// Single word names also seem affected
// Expected: "Jo" but getting something else
console.log(getInitials('John'));
```

### Expected behavior

The function should return the first letters of each word in the name:
- "John Doe" → "JD"
- "John Doe Smith" with limit 3 → "JDS"
- "John" → "JO"

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
