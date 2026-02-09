# Bug Report

### Indicator positioning broken for center and middle positions

I'm experiencing an issue with the `Indicator` component where the positioning is completely off when using `middle` or `center` positions. The indicator appears to be shifted away from where it should be instead of being properly centered.

### Reproduction

```jsx
import { Indicator, Avatar } from '@mantine/core';

// This renders the indicator in the wrong position
<Indicator position="middle-center">
  <Avatar src="avatar.png" />
</Indicator>

// Also broken with middle-start and middle-end
<Indicator position="middle-start">
  <Avatar src="avatar.png" />
</Indicator>

// Same issue with top-center and bottom-center
<Indicator position="top-center">
  <Avatar src="avatar.png" />
</Indicator>
```

### Expected behavior

When using `position="middle-center"`, the indicator should be centered both horizontally and vertically on the target element. Currently it appears to be offset in the wrong direction - instead of being centered, it's shifted outward from the element.

Similarly, `position="middle-start"` and `position="middle-end"` should center the indicator vertically along the middle of the element, but they're also positioned incorrectly.

The same centering issue occurs with any position that uses `center` placement (like `top-center`, `bottom-center`).

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
