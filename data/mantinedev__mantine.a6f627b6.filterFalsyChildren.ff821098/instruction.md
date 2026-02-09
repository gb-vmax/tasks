# Bug Report

### Describe the bug

When using `Group` component with children that include `null` or `undefined` values, the component doesn't filter them out correctly. This causes rendering issues where falsy children are still being processed instead of being removed.

### Reproduction

```jsx
import { Group, Button } from '@mantine/core';

function MyComponent() {
  const showButton = false;
  
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

The `null` and `undefined` values are not being filtered out properly, which can lead to unexpected behavior in the layout.

### Expected behavior

The `Group` component should automatically filter out `null` and `undefined` children, so only valid React elements are rendered. This is standard behavior for most component libraries when dealing with conditional rendering.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
