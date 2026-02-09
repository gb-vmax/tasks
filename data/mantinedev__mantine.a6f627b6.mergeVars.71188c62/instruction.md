# Bug Report

### Describe the bug

When using components with multiple CSS variables defined through the `vars` prop, only the last set of variables is being applied. Variables from earlier entries are getting completely overwritten instead of being merged together.

### Reproduction

```jsx
import { Box } from '@mantine/core';

// Define multiple sets of CSS variables
const Component = () => (
  <Box
    vars={(theme) => [
      { root: { '--color-primary': 'red', '--size': '10px' } },
      { root: { '--color-secondary': 'blue', '--padding': '20px' } }
    ]}
  >
    Content
  </Box>
);
```

### Expected behavior

All CSS variables from both objects should be merged and applied:
- `--color-primary: red`
- `--size: 10px`
- `--color-secondary: blue`
- `--padding: 20px`

### Actual behavior

Only the variables from the second object are applied:
- `--color-secondary: blue`
- `--padding: 20px`

The first set of variables (`--color-primary` and `--size`) are lost.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
