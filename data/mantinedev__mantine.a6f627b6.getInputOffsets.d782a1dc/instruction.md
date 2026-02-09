# Bug Report

### Describe the bug

The `InputWrapper` component is incorrectly calculating input offsets when description or error messages are present. The spacing above and below the input field appears to be swapped - elements that should add spacing above the input are adding spacing below, and vice versa.

### Reproduction

```jsx
import { Input } from '@mantine/core';

// Case 1: Description above input
<Input.Wrapper
  description="This is a description"
  inputWrapperOrder={['description', 'input', 'error']}
>
  <Input />
</Input.Wrapper>

// Case 2: Error below input
<Input.Wrapper
  error="This is an error"
  inputWrapperOrder={['input', 'error']}
>
  <Input />
</Input.Wrapper>
```

### Expected behavior

- When description/error is positioned above the input (appears before 'input' in `inputWrapperOrder`), `offsetTop` should be true
- When description/error is positioned below the input (appears after 'input' in `inputWrapperOrder`), `offsetBottom` should be true

### Actual behavior

The offsets are reversed - top spacing is applied when elements are below, and bottom spacing is applied when elements are above.

### System Info

- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
