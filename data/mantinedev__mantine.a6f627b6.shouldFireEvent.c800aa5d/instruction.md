# Bug Report

### Describe the bug

The `useHotkeys` hook is firing keyboard shortcuts even when the user is typing in input fields, textareas, or contentEditable elements. This causes unwanted behavior where hotkeys are triggered while users are trying to enter text.

### Reproduction

```jsx
import { useHotkeys } from '@mantine/hooks';

function MyComponent() {
  useHotkeys([
    ['mod+K', () => console.log('Hotkey triggered!')],
  ]);

  return (
    <div>
      <input type="text" placeholder="Type here" />
      <textarea placeholder="Or here" />
      <div contentEditable>Or edit this</div>
    </div>
  );
}
```

Steps to reproduce:
1. Focus on any of the input fields, textarea, or contentEditable div
2. Press `Ctrl+K` (or `Cmd+K` on Mac) while typing
3. The hotkey handler fires even though you're in an editable field

### Expected behavior

Hotkeys should be ignored when the user is focused on input fields, textareas, select elements, or contentEditable elements by default. The shortcuts should only trigger when focus is outside these elements, unless explicitly configured otherwise with `triggerOnContentEditable`.

### System Info

- @mantine/hooks version: latest
- React version: 18.x
- Browser: Chrome/Firefox

---
Repository: /testbed
