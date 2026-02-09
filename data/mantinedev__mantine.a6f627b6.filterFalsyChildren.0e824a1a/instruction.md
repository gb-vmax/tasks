# Bug Report

### Describe the bug

I'm experiencing an issue with the `Group` component where falsy children (like `null`, `undefined`, `false`) are not being filtered out properly. The component is rendering empty spaces or throwing errors when these falsy values are passed as children.

### Reproduction

```jsx
import { Group, Button } from '@mantine/core';

function MyComponent() {
  const showButton = false;
  
  return (
    <Group>
      <Button>Always visible</Button>
      {showButton && <Button>Conditionally visible</Button>}
      {null}
      {undefined}
      <Button>Another button</Button>
    </Group>
  );
}
```

### Expected behavior

The `Group` component should filter out all falsy children (`null`, `undefined`, `false`, etc.) and only render the actual valid React elements. Empty spaces or errors should not appear in the rendered output.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
