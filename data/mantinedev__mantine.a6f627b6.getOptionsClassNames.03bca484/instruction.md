# Bug Report

### Describe the bug

I'm experiencing an issue with the styles API where component classNames aren't being applied correctly. It seems like the props being passed to `resolveClassNames` aren't being prioritized properly, causing styles to not apply as expected.

### Reproduction

```jsx
import { Button } from '@mantine/core';

function MyComponent() {
  return (
    <Button
      classNames={{
        root: 'my-custom-class'
      }}
    >
      Click me
    </Button>
  );
}
```

When I pass custom classNames through the component props, they don't seem to be applied. The component renders but my custom classes are missing from the DOM.

### Expected behavior

Custom classNames passed via props should be applied to the component elements. The `my-custom-class` should appear on the button's root element.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Firefox 121

---
Repository: /testbed
