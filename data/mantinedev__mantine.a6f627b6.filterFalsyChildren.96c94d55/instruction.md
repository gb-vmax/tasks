# Bug Report

### Describe the bug

I'm experiencing an issue with the `Group` component where child elements are not rendering correctly. Instead of displaying the actual React components, it seems like only the props objects are being rendered.

### Reproduction

```jsx
import { Group, Button } from '@mantine/core';

function MyComponent() {
  return (
    <Group>
      <Button>Click me</Button>
      <Button>Another button</Button>
    </Group>
  );
}
```

When this renders, the buttons don't appear as expected. It looks like the component structure is broken and only plain objects are being passed through.

### Expected behavior

The `Group` component should render its children normally. Each child component (like `Button`) should be displayed as a fully functional React element.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
