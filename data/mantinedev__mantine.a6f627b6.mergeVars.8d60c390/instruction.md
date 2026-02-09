# Bug Report

### Describe the bug

I'm experiencing an issue with CSS variable resolution in components where the first set of CSS variables in the array is being completely ignored, and the merge order seems to be reversed. When multiple variable objects are provided, only variables from the second object onwards are applied, and when there are conflicts, the wrong values take precedence.

### Reproduction

```tsx
const vars = [
  { root: { '--color-primary': 'red' } },
  { root: { '--color-primary': 'blue', '--color-secondary': 'green' } }
];

// After merging, expected result:
// { root: { '--color-primary': 'blue', '--color-secondary': 'green' } }

// Actual result:
// { root: { '--color-secondary': 'green' } }
// The first object is skipped entirely, and '--color-primary' from the second object is missing
```

Also noticed that when variables should override each other, the precedence is backwards:

```tsx
const vars = [
  { root: { '--spacing': '16px' } },
  { root: { '--spacing': '24px' } }
];

// Expected: '--spacing' should be '24px' (later values override earlier ones)
// Actual: '--spacing' is '16px' (earlier values override later ones)
```

### Expected behavior

1. All variable objects in the array should be processed, including the first one
2. When merging variables with the same key, later values should override earlier values (standard merge behavior)

### System Info

- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
