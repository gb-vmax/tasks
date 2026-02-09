# Bug Report

### CSS variables not merging correctly with custom generator

I'm experiencing an issue where custom CSS variables defined through a `cssVariablesResolver` are not being applied correctly. It seems like the default variables are completely overriding my custom ones instead of merging them together.

### Reproduction

```tsx
import { MantineProvider, createTheme } from '@mantine/core';

const theme = createTheme({
  // ... theme config
});

const customResolver = (theme) => ({
  variables: {
    '--my-custom-var': 'value1',
  },
  light: {
    '--custom-light': 'lightValue',
  },
  dark: {
    '--custom-dark': 'darkValue',
  },
});

<MantineProvider theme={theme} cssVariablesResolver={customResolver}>
  <App />
</MantineProvider>
```

### Expected behavior

Both the default Mantine CSS variables and my custom variables should be present in the DOM. The custom variables should merge with (or override) the defaults where there are conflicts.

### Actual behavior

Either the custom variables are completely missing, or the default Mantine variables are not being applied at all. It's like one set is completely replacing the other instead of merging.

This is blocking me from customizing the theme properly since I need both the default Mantine variables and my custom additions.

---
Repository: /testbed
