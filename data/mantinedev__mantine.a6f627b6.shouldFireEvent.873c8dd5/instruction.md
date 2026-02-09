# Bug Report

### Describe the bug

Hotkeys are firing in input fields and textareas when they shouldn't be. The `useHotkeys` hook is triggering keyboard shortcuts even when the user is typing in form elements, which breaks the normal typing experience.

### Reproduction

```jsx
import { useHotkeys } from '@mantine/hooks';

function MyComponent() {
  useHotkeys([
    ['ctrl+K', () => console.log('Shortcut triggered!')],
  ]);

  return (
    <div>
      <input type="text" placeholder="Try typing ctrl+K here" />
      <textarea placeholder="Or here" />
    </div>
  );
}
```

When typing in the input field or textarea, pressing `ctrl+K` triggers the hotkey callback instead of just typing normally. The hotkey should be ignored when focus is inside these form elements.

### Expected behavior

Hotkeys should not fire when the user is typing in input fields, textareas, or other editable elements. This is standard behavior to prevent shortcuts from interfering with normal text input.

### System Info
- @mantine/hooks version: latest
- React version: 18.x
- Browser: Firefox/Chrome

---
Repository: /testbed
