# Bug Report

### Describe the bug

When using the `Group` component with conditional children, some falsy values like `null` and `undefined` are not being filtered out correctly. This causes React to throw warnings or render unexpected content.

### Reproduction

```jsx
import { Group, Button } from '@mantine/core';

function MyComponent({ showButton }) {
  return (
    <Group>
      <Button>Always visible</Button>
      {showButton && <Button>Conditional</Button>}
      {null}
      {undefined}
      <Button>Another button</Button>
    </Group>
  );
}
```

When `showButton` is false, the conditional rendering returns `false`, but other falsy values like `null` and `undefined` seem to be treated differently now. This results in React warnings about invalid children.

### Expected behavior

All falsy children (including `null`, `undefined`, `false`, `0`, empty strings, etc.) should be filtered out consistently so that only valid React elements are rendered within the Group component.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
