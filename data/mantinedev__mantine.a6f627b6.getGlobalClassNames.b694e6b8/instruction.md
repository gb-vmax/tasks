# Bug Report

### Describe the bug

Focus styles are not being applied to focusable components. When setting `focusable` prop on components, the focus ring/outline doesn't appear when the element receives focus.

### Reproduction

```jsx
import { Button } from '@mantine/core';

function Demo() {
  return (
    <Button focusable>
      Click me and try to focus
    </Button>
  );
}
```

### Steps to reproduce:
1. Create a component with `focusable` prop set to true
2. Click or tab to focus the element
3. Notice that no focus ring appears

### Expected behavior

When a component has the `focusable` option enabled, it should display the theme's focus ring styles (either the custom `focusClassName` or the default focus ring based on `theme.focusRing` setting). The focus styles should be visible when the element receives keyboard or programmatic focus.

### Additional context

This seems to have broken recently. The focus ring was working fine before and now it's completely missing on all focusable elements. Tested with both default theme settings and custom focus class names.

---
Repository: /testbed
