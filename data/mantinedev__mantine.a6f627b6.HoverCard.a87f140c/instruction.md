# Bug Report

### Describe the bug

The HoverCard component is not displaying correctly - it appears to be showing when it should be hidden and hiding when it should be visible. Additionally, hovering over the target element seems to close the card instead of opening it.

### Reproduction

```jsx
import { HoverCard, Text, Button } from '@mantine/core';

function Demo() {
  return (
    <HoverCard>
      <HoverCard.Target>
        <Button>Hover over me</Button>
      </HoverCard.Target>
      <HoverCard.Dropdown>
        <Text>This should appear on hover</Text>
      </HoverCard.Dropdown>
    </HoverCard>
  );
}
```

### Expected behavior

- The dropdown should be hidden by default
- When hovering over the target element, the dropdown should appear
- When moving the mouse away, the dropdown should disappear

### Actual behavior

- The dropdown appears to be visible by default
- Hovering over the target makes the dropdown disappear
- The behavior is completely inverted from what it should be

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome/Firefox

This seems like a recent regression as it was working fine before. Any help would be appreciated!

---
Repository: /testbed
