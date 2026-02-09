# Bug Report

### Describe the bug

I'm experiencing unexpected behavior with the `useFocusWithin` hook. When focusing in and out of elements, the focus state seems to be inverted or triggering incorrectly. The `focused` state becomes true when it shouldn't be, and the blur callbacks are firing at the wrong times.

### Reproduction

```jsx
import { useFocusWithin } from '@mantine/hooks';

function MyComponent() {
  const { ref, focused } = useFocusWithin();
  
  return (
    <div ref={ref}>
      <input type="text" />
      <p>Focused: {focused.toString()}</p>
    </div>
  );
}
```

Steps to reproduce:
1. Click inside the input element
2. Click outside the container div
3. The `focused` state remains true even though focus has left the container

### Expected behavior

The `focused` state should be `true` only when focus is within the container element and its children. When clicking outside the container, `focused` should become `false`.

Currently it seems like the focus detection logic is backwards - it's reporting focused when it should be blurred and vice versa.

### System Info
- @mantine/hooks version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
