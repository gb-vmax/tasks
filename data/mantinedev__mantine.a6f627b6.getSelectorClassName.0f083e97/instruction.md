# Bug Report

### Describe the bug

When using the `unstyled` prop on Mantine components, the styles are being applied instead of being removed. It seems like the behavior is inverted - components with `unstyled={true}` are showing styles, while components with `unstyled={false}` (or no unstyled prop) are not showing any styles.

### Reproduction

```jsx
import { Button } from '@mantine/core';

// This button should have no styles but styles are applied
<Button unstyled>Click me</Button>

// This button should have styles but appears unstyled
<Button>Click me</Button>
```

### Expected behavior

- When `unstyled={true}` is set, the component should render without any library styles
- When `unstyled={false}` or when the prop is not provided, the component should render with the default Mantine styles

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
