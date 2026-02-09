# Bug Report

### Describe the bug

When using floating components (like Tooltip, Popover, etc.) with RTL (right-to-left) direction, the positioning is not working correctly. The floating element appears on the wrong side of the target element.

### Reproduction

```jsx
import { Tooltip } from '@mantine/core';

// Set direction to RTL
<MantineProvider theme={{ dir: 'rtl' }}>
  <Tooltip label="Test tooltip" position="right">
    <button>Hover me</button>
  </Tooltip>
</MantineProvider>

// Expected: Tooltip should appear on the LEFT side (flipped for RTL)
// Actual: Tooltip appears on the RIGHT side (not flipped)
```

The same issue occurs with `position="left"` - it doesn't flip to the right side as expected in RTL mode.

### Expected behavior

In RTL mode, horizontal positions should be flipped:
- `position="right"` should render on the left
- `position="left"` should render on the right

This is the standard behavior for RTL layouts to maintain logical positioning.

### System Info

- @mantine/core version: latest
- Browser: All browsers
- Direction: RTL

---
Repository: /testbed
