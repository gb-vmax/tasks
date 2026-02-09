# Bug Report

### Describe the bug

When using the styles API with `unstyled` prop set to `false` (or not set at all), components are not receiving their proper CSS classes. The styling seems to be completely broken and components render without any of their default styles.

### Reproduction

```jsx
import { Button } from '@mantine/core';

function App() {
  return (
    // This button renders without any styles
    <Button>Click me</Button>
  );
}
```

Or explicitly setting `unstyled={false}`:

```jsx
<Button unstyled={false}>Click me</Button>
```

### Expected behavior

Components should apply their default CSS classes and render with proper styling when `unstyled` is `false` or not specified. Only when `unstyled={true}` should the styles be removed.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
