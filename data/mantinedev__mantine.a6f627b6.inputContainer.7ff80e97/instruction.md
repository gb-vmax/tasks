# Bug Report

### Describe the bug

The `InputWrapper` component is not rendering correctly when `inputContainer` prop receives an array of children. Instead of rendering all children in the array, only the first child is being displayed.

### Reproduction

```jsx
import { InputWrapper } from '@mantine/core';

function Demo() {
  return (
    <InputWrapper
      label="Example"
      inputContainer={(children) => (
        <div>
          {children}
        </div>
      )}
    >
      <input type="text" />
      <button>Submit</button>
    </InputWrapper>
  );
}
```

When passing multiple children to the `InputWrapper`, only the first child (the input) is rendered. The button doesn't appear in the output.

### Expected behavior

All children passed to `inputContainer` should be rendered, not just the first element of the array. When multiple children are provided, they should all be displayed in the wrapper.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
