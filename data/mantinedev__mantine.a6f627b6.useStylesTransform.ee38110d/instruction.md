# Bug Report

### Describe the bug

I'm experiencing an issue where custom styles transforms are not being applied to components. When I provide a `stylesTransform` function through the `MantineProvider`, the transformed styles are not being used and components render with their default styling instead.

### Reproduction

```tsx
import { MantineProvider } from '@mantine/core';

const stylesTransform = (styles, context) => {
  // Custom transformation logic
  return {
    ...styles,
    customProperty: 'customValue'
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

The `stylesTransform` function should be called and the transformed styles should be applied to the components. The custom properties added by the transform should be visible in the rendered output.

### Actual behavior

The `stylesTransform` function appears to be ignored completely. Components render with their default theme styles and any custom transformations are not applied.

This was working fine in previous versions but seems to have broken recently. Not sure if this is a regression or if I'm missing something in the setup.

---
Repository: /testbed
