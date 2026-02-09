# Bug Report

### Describe the bug

The HoverCard component is behaving in reverse - it shows when it should be hidden and hides when it should be visible. When I hover over the trigger element, nothing appears, but when I move my mouse away, the card suddenly shows up.

### Reproduction

```jsx
import { HoverCard, Text, Button } from '@mantine/core';

function Demo() {
  return (
    <HoverCard width={280} shadow="md">
      <HoverCard.Target>
        <Button>Hover over me</Button>
      </HoverCard.Target>
      <HoverCard.Dropdown>
        <Text size="sm">
          This should appear on hover
        </Text>
      </HoverCard.Dropdown>
    </HoverCard>
  );
}
```

### Expected behavior

- Hovering over the button should open the dropdown
- Moving the mouse away should close the dropdown

### Actual behavior

- Hovering over the button does nothing (dropdown stays hidden)
- Moving the mouse away causes the dropdown to appear
- The behavior is completely inverted

This seems to have broken recently. The component worked fine before and now it's doing the opposite of what it should.

---
Repository: /testbed
