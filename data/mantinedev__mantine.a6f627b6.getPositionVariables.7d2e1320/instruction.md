# Bug Report

### Describe the bug

The Indicator component is not positioning correctly when using `middle` or `center` positions. The indicator appears in the wrong location on the screen instead of being centered as expected.

### Reproduction

```tsx
import { Indicator } from '@mantine/core';

// This doesn't center vertically as expected
<Indicator position="middle-start">
  <div>Content</div>
</Indicator>

// This doesn't center horizontally as expected
<Indicator position="top-center">
  <div>Content</div>
</Indicator>
```

When setting `position="middle-start"` or `position="middle-end"`, the indicator should be vertically centered but it's not. Similarly, when using `position="top-center"` or `position="bottom-center"`, the indicator should be horizontally centered but appears in the wrong position.

### Expected behavior

- `middle` positions (like `middle-start`, `middle-end`) should vertically center the indicator
- `center` positions (like `top-center`, `bottom-center`) should horizontally center the indicator

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
