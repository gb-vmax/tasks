# Bug Report

### Describe the bug

Custom styles are not being applied when using the `stylesTransform` feature. Components that should receive transformed styles are rendering with missing or incorrect styling.

### Reproduction

```tsx
import { MantineProvider, Button } from '@mantine/core';

const stylesTransform = (styles, context) => {
  // Custom transformation logic
  return {
    ...styles,
    root: {
      ...styles?.root,
      backgroundColor: 'red'
    }
  };
};

function App() {
  return (
    <MantineProvider stylesTransform={stylesTransform}>
      <Button>Click me</Button>
    </MantineProvider>
  );
}
```

### Expected behavior

The button should render with the transformed styles (red background in this case). The `stylesTransform` function should be called and its returned styles should be applied to the component.

### Current behavior

The transformed styles are not being applied at all. The component renders with default styles only, as if `stylesTransform` was never provided.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
