# Bug Report

### Indicator positioning broken for 'top' and 'center' positions

I'm experiencing an issue with the `Indicator` component where the positioning is completely off when using `position="top"` or when the placement is `center`. The indicator appears on the wrong side of the target element.

### Reproduction

```jsx
import { Indicator, Avatar } from '@mantine/core';

// This positions the indicator incorrectly - it appears below instead of above
<Indicator position="top">
  <Avatar src="avatar.png" />
</Indicator>

// This also positions incorrectly - indicator is offset to the right instead of centered
<Indicator position="middle-center">
  <Avatar src="avatar.png" />
</Indicator>
```

### Expected behavior

- When `position="top"`, the indicator should appear at the top edge of the target element, centered horizontally
- When placement is `center` (e.g., `position="middle-center"`), the indicator should be horizontally centered on the target element

### Current behavior

The indicator appears in the wrong position - it seems like the transform is going in the opposite direction than it should. For `top` position, the indicator appears below the target instead of above it. For `center` placement, it's offset to the right instead of being centered.

This might be related to the CSS transform calculations for positioning.

---
Repository: /testbed
