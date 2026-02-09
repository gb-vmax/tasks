# Bug Report

### Describe the bug

I'm experiencing an issue with static class names not being generated correctly for Mantine components. When I inspect the DOM, the class names appear to be malformed and components aren't receiving their expected static classes.

### Reproduction

```jsx
import { Button } from '@mantine/core';

function App() {
  return <Button>Click me</Button>;
}
```

When inspecting the button element in the browser, I notice:
1. The static class names are not being applied when they should be
2. When they are applied, the class name format looks wrong - it seems like parts of the class name are being duplicated instead of including the component name

### Expected behavior

Components should receive properly formatted static class names like `mantine-Button-root`, `mantine-Input-wrapper`, etc. These classes should be applied by default unless explicitly disabled with `withStaticClass={false}`.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
