# Bug Report

### Describe the bug

Keyboard navigation is not working properly in components that use scoped keydown handlers. When pressing arrow keys to navigate between sibling elements, the focus moves to incorrect elements or doesn't move at all. Additionally, Home and End keys seem to focus on disabled elements instead of skipping them.

### Reproduction

```jsx
import { Button } from '@mantine/core';

function MyComponent() {
  return (
    <div>
      <Button>First</Button>
      <Button>Second</Button>
      <Button disabled>Third (disabled)</Button>
      <Button>Fourth</Button>
    </div>
  );
}
```

Steps to reproduce:
1. Create a component with multiple focusable sibling elements
2. Try using arrow keys to navigate between them
3. Press Home or End keys

### Expected behavior

- Arrow keys should navigate to the next/previous sibling element on the same level
- Home key should focus the first **enabled** element
- End key should focus the last **enabled** element
- Disabled elements should be skipped during navigation

### Actual behavior

- Arrow keys navigate to elements that are not on the same level or skip valid siblings
- Home/End keys focus on disabled elements instead of skipping them

### System Info

- @mantine/core version: latest
- Browser: Chrome/Firefox
- OS: macOS/Windows

This is affecting keyboard accessibility in my application. Any help would be appreciated!

---
Repository: /testbed
