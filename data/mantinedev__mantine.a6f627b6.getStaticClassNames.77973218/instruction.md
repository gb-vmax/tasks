# Bug Report

### Describe the bug

The static class names are not being applied to components when `withStaticClass` is enabled. Additionally, the order of the generated class name segments appears to be incorrect.

### Reproduction

```jsx
import { Button } from '@mantine/core';

// With withStaticClass enabled
<Button withStaticClass>Click me</Button>
```

When inspecting the element, the expected static class names like `mantine-Button-root` are missing from the component. The class name structure seems to have the theme name and selector in the wrong order.

### Expected behavior

When `withStaticClass` is set (or defaults to true), components should have static class names applied in the format `${classNamesPrefix}-${themeName}-${selector}` (e.g., `mantine-Button-root`). These class names should be present in the DOM for styling and testing purposes.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome/Firefox

---
Repository: /testbed
