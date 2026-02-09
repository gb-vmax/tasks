# Bug Report

### Describe the bug

The `useHotkeys` hook is not working correctly - hotkeys are firing in the wrong contexts. Specifically:

1. When `triggerOnContentEditable` is set to `true`, hotkeys are **only** firing on elements that should be ignored (like INPUT, TEXTAREA, etc.) instead of firing everywhere except those elements
2. When `triggerOnContentEditable` is `false` (default), hotkeys are **only** firing on contentEditable elements instead of firing on non-contentEditable elements

This is essentially inverted behavior - the hook is doing the opposite of what it should be doing.

### Reproduction

```tsx
import { useHotkeys } from '@mantine/hooks';

function App() {
  useHotkeys([
    ['ctrl+K', () => console.log('Hotkey triggered!')]
  ]);

  return (
    <div>
      <input type="text" placeholder="Type here" />
      <button>Click me</button>
      <div contentEditable>Editable content</div>
    </div>
  );
}
```

**What happens:**
- Pressing `ctrl+K` while focused on the input field triggers the hotkey (should be ignored)
- Pressing `ctrl+K` while focused on the button does NOT trigger the hotkey (should work)

**With `triggerOnContentEditable: true`:**
```tsx
useHotkeys([
  ['ctrl+K', () => console.log('Hotkey triggered!'), { triggerOnContentEditable: true }]
]);
```
- Hotkeys only fire when focused on INPUT/TEXTAREA elements (completely wrong)
- Hotkeys don't fire on regular elements or contentEditable elements

### Expected behavior

Hotkeys should:
- Fire on regular elements (buttons, divs, etc.)
- NOT fire on form inputs (INPUT, TEXTAREA, SELECT) by default
- NOT fire on contentEditable elements by default
- When `triggerOnContentEditable: true`, fire on contentEditable elements but still ignore form inputs

### System Info
- @mantine/hooks version: latest
- React version: 18.x

---
Repository: /testbed
