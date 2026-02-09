# Bug Report

### Describe the bug

CSS variables defined in component-level `vars` functions are not being applied correctly. When defining custom CSS variables through the component's `vars` function, they seem to be overridden or not merged properly with theme-level variables.

### Reproduction

```tsx
import { createTheme, MantineProvider } from '@mantine/core';

const theme = createTheme({
  components: {
    Button: {
      vars: (theme, props) => ({
        root: {
          '--button-custom-color': props.color || 'blue',
        },
      }),
    },
  },
});

// Component-level vars are not being applied as expected
<MantineProvider theme={theme}>
  <Button color="red">Click me</Button>
</MantineProvider>
```

### Expected behavior

Component-level CSS variables should be properly merged and applied. The `--button-custom-color` variable should be set to 'red' in this case, but it appears that the variable resolution order is incorrect, causing component vars to be ignored or overridden.

### System Info

- @mantine/core version: 7.x
- React version: 18.x
- Browser: Chrome/Firefox

---
Repository: /testbed
