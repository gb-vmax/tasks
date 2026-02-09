# Bug Report

### Describe the bug

I'm experiencing an issue with the styles API where class names are not being resolved correctly. When using custom `classNames` prop with components, the styles are not being applied as expected.

### Reproduction

```jsx
import { Button } from '@mantine/core';

function Demo() {
  return (
    <Button
      classNames={{
        root: 'custom-button',
        label: 'custom-label'
      }}
    >
      Click me
    </Button>
  );
}
```

The custom class names defined in the `classNames` prop don't seem to be getting applied to the component. The component renders but without the expected styling.

### Expected behavior

The component should apply the custom class names specified in the `classNames` prop to the appropriate elements. The `root` class should be applied to the button wrapper and `label` class to the button label.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome 120

---
Repository: /testbed
