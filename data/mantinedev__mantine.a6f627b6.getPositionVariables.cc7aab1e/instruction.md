# Bug Report

### Describe the bug

The `Indicator` component is not positioning correctly when using certain position values. Specifically, when using positions like `'middle'` or `'center'`, the indicator appears in the wrong location instead of being centered properly.

### Reproduction

```jsx
import { Indicator } from '@mantine/core';

// This should center the indicator vertically
<Indicator position="middle" offset={10}>
  <div>Content</div>
</Indicator>

// This should center the indicator horizontally
<Indicator position="top-center" offset={5}>
  <div>Content</div>
</Indicator>
```

### Expected behavior

- When `position="middle"` is used, the indicator should be vertically centered (at 50% from the top with proper translation)
- When using positions with `center` placement (like `"top-center"`), the indicator should be horizontally centered with a `-50%` transform to properly center it

### Actual behavior

The indicator is positioned incorrectly - it appears offset from where it should be. The centering logic doesn't seem to be working as expected.

### System Info

- @mantine/core version: latest
- Browser: Chrome

---
Repository: /testbed
