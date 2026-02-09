# Bug Report

### Describe the bug

The visibility toggle button in `PasswordInput` doesn't prevent the default mousedown behavior anymore, which causes the input field to lose focus when clicking the toggle button. This is particularly noticeable when the input is focused and you try to toggle password visibility - the input immediately loses focus after clicking.

### Reproduction

```jsx
import { PasswordInput } from '@mantine/core';

function Demo() {
  return (
    <PasswordInput
      label="Password"
      placeholder="Enter password"
      visibilityToggleButtonProps={{
        onMouseDown: (event) => {
          console.log('mousedown event:', event);
        }
      }}
    />
  );
}
```

Steps to reproduce:
1. Render a PasswordInput component
2. Focus the input field by clicking on it
3. Click the visibility toggle button (eye icon)
4. Notice that the input loses focus

### Expected behavior

The input field should remain focused when clicking the visibility toggle button. The button click should only toggle password visibility without affecting the input's focus state.

### Additional context

This appears to be related to how the `onMouseDown` event is handled on the visibility toggle button. The event object should be passed to the custom `onMouseDown` handler if provided via `visibilityToggleButtonProps`.

---
Repository: /testbed
