# Bug Report

### Describe the bug

The `useHotkeys` hook is firing keyboard shortcuts even when typing in input fields, textareas, and contentEditable elements. This is causing unexpected behavior where hotkeys trigger while users are trying to enter text in form fields.

### Reproduction

```jsx
import { useHotkeys } from '@mantine/hooks';

function MyComponent() {
  useHotkeys([
    ['mod+S', () => console.log('Save triggered')],
  ]);

  return (
    <div>
      <input type="text" placeholder="Type here" />
      <textarea placeholder="Type here too" />
    </div>
  );
}
```

Steps to reproduce:
1. Focus on the input field or textarea
2. Press Ctrl+S (or Cmd+S on Mac)
3. The hotkey handler fires even though you're typing in a text field

### Expected behavior

Hotkeys should NOT trigger when the user is focused on input fields, textareas, select elements, or contentEditable elements. The hook should ignore these events by default to prevent interfering with normal text input.

### System Info
- @mantine/hooks version: latest
- React version: 18.x
- Browser: Chrome/Firefox/Safari

This is a pretty critical issue as it makes forms unusable when hotkeys are enabled. Any workaround in the meantime?

---
Repository: /testbed
