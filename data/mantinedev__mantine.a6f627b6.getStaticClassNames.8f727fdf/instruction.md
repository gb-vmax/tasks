# Bug Report

### Describe the bug

The static class names generation is not working as expected. When `withStaticClass` is set to `true` (or not explicitly set to `false`), no class names are being generated. Additionally, when class names are generated, the order of the theme name and selector in the class name string appears to be incorrect.

### Reproduction

```tsx
import { getStaticClassNames } from '@mantine/core';

// Case 1: withStaticClass is true or undefined
const result1 = getStaticClassNames({
  themeName: ['Button'],
  classNamesPrefix: 'mantine',
  selector: 'root',
  withStaticClass: true
});

console.log(result1); // Expected: ['mantine-Button-root'], Actual: []

// Case 2: withStaticClass is false
const result2 = getStaticClassNames({
  themeName: ['Button'],
  classNamesPrefix: 'mantine',
  selector: 'root',
  withStaticClass: false
});

console.log(result2); // Expected: [], but getting class names instead

// Case 3: Multiple theme names
const result3 = getStaticClassNames({
  themeName: ['Button', 'UnstyledButton'],
  classNamesPrefix: 'mantine',
  selector: 'root',
  withStaticClass: true
});

console.log(result3); 
// Expected: ['mantine-Button-root', 'mantine-UnstyledButton-root']
// Actual: [] (and even if it worked, the format seems wrong)
```

### Expected behavior

- When `withStaticClass` is `true` or `undefined`, the function should return an array of properly formatted class names
- When `withStaticClass` is `false`, it should return an empty array
- The class name format should follow the pattern: `${classNamesPrefix}-${themeName}-${selector}`

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
