# Bug Report

### Describe the bug

The `useFocusWithin` hook is not working correctly when handling focus events. When moving focus between elements inside a container, the hook's state updates unexpectedly or doesn't update when it should.

### Reproduction

```jsx
import { useFocusWithin } from '@mantine/hooks';

function Demo() {
  const { ref, focused } = useFocusWithin();
  
  return (
    <div ref={ref}>
      <input type="text" />
      <button>Click me</button>
      <p>Focused: {focused.toString()}</p>
    </div>
  );
}
```

Steps to reproduce:
1. Create a component with multiple focusable elements inside a container
2. Use `useFocusWithin` hook on the container
3. Tab between the input and button elements
4. The `focused` state behaves incorrectly - it may show as unfocused when focus is still within the container, or remain focused when moving focus outside

### Expected behavior

The `focused` state should be `true` when any element inside the container has focus, and `false` only when focus moves completely outside the container. Moving focus between child elements should maintain the focused state.

### System Info
- @mantine/hooks version: latest
- React version: 18.x
- Browser: Chrome/Firefox

---
Repository: /testbed
