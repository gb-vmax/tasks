# Bug Report

### Describe the bug

When using component theming with `vars` in headless mode, the vars are not being applied correctly. It seems like in headless mode, the component-level `vars` function is being ignored and not included in the final styles.

### Reproduction

```tsx
import { createTheme, MantineProvider } from '@mantine/core';
import { Button } from '@mantine/core';

const theme = createTheme({
  components: {
    Button: {
      vars: (theme, props) => ({
        root: {
          '--button-custom-var': 'red'
        }
      })
    }
  }
});

function App() {
  return (
    <MantineProvider theme={theme}>
      <Button headless vars={(theme, props) => ({
        root: {
          '--button-override': 'blue'
        }
      })}>
        Click me
      </Button>
    </MantineProvider>
  );
}
```

### Expected behavior

When using `headless` mode with a component that has custom `vars` defined, those vars should still be applied to the component. The vars passed directly to the component should override any theme-level vars.

### Actual behavior

In headless mode, the `vars` prop seems to be completely ignored and the custom CSS variables are not applied to the component.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
