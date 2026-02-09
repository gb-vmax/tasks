# Bug Report

### Describe the bug

Static class names are being generated in the wrong order and the `withStaticClass` logic seems to be inverted. When `withStaticClass` is not explicitly set to `true`, static classes are not being applied at all, and when they are applied, the order of the class name parts is incorrect.

### Reproduction

```tsx
import { useStyles } from '@mantine/core';

// Case 1: withStaticClass undefined or null
const { classes } = useStyles({
  themeName: ['Button', 'root'],
  classNamesPrefix: 'mantine',
  selector: 'button',
  withStaticClass: undefined, // or null
});

console.log(classes); // Expected: static classes, Actual: empty array

// Case 2: Class name order issue
const { classes } = useStyles({
  themeName: ['Button', 'root'],
  classNamesPrefix: 'mantine',
  selector: 'button',
  withStaticClass: true,
});

console.log(classes);
// Expected: ['mantine-Button-button', 'mantine-root-button']
// Actual: ['mantine-button-Button', 'mantine-button-root']
```

### Expected behavior

1. When `withStaticClass` is not explicitly `false`, static class names should be generated
2. The class name format should follow the pattern: `{prefix}-{themeName}-{selector}`, not `{prefix}-{selector}-{themeName}`

### System Info

- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
