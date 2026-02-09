# Bug Report

### Describe the bug
When using `classNames` with component options, the props are not being passed correctly to the `resolveClassNames` function. Instead of receiving the actual component props, it's receiving the entire options object, which causes styles to not be applied properly based on prop values.

### Reproduction
```jsx
import { Button } from '@mantine/core';

const MyButton = () => {
  return (
    <Button
      classNames={{
        root: 'custom-root'
      }}
      size="lg"
      variant="filled"
    >
      Click me
    </Button>
  );
};
```

When the button is rendered, the styles that depend on props like `size` or `variant` are not being applied correctly. The component receives the options object instead of the actual props, so conditional styling based on prop values doesn't work.

### Expected behavior
The component should receive the correct props and apply styles based on them. Prop-dependent classNames should be resolved properly.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
