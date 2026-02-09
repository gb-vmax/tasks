# Bug Report

### Describe the bug

When using custom `varsResolver` with components, the CSS variables are not being applied correctly. It seems like the `varsResolver` function is being ignored or not merged properly into the final styles, causing custom CSS variables to not appear in the rendered output.

### Reproduction

```tsx
import { createTheme, MantineProvider } from '@mantine/core';

const theme = createTheme({
  components: {
    Button: {
      vars: (theme, props) => ({
        root: {
          '--button-custom-var': '10px',
        },
      }),
    },
  },
});

function Demo() {
  return (
    <MantineProvider theme={theme}>
      <Button>Test Button</Button>
    </MantineProvider>
  );
}
```

The custom CSS variable `--button-custom-var` is not being applied to the button element. When inspecting the DOM, the variable is missing from the component's style attributes.

### Expected behavior

The `varsResolver` should be properly merged and the custom CSS variables should be present in the rendered component's styles. The variable `--button-custom-var` should appear in the button's inline styles or style object.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
