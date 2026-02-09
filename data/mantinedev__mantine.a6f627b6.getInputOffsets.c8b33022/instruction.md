# Bug Report

### Describe the bug

The `InputWrapper` component is incorrectly applying offsets to input elements when `description` or `error` are positioned above the input field. The offset logic seems to be reversed - elements that should be above the input are being treated as if they're below it.

### Reproduction

```jsx
import { Input } from '@mantine/core';

// Configure input wrapper with description above input
<Input.Wrapper
  label="Username"
  description="Enter your username"
  inputWrapperOrder={['label', 'description', 'input', 'error']}
>
  <Input />
</Input.Wrapper>
```

When the `description` is positioned above the `input` in the `inputWrapperOrder`, the offset calculations are incorrect. The component doesn't properly calculate spacing for elements that appear before the input field.

### Expected behavior

The `InputWrapper` should correctly identify which elements (description/error) are positioned above vs below the input field and apply appropriate offsets. Elements in the `inputWrapperOrder` array that come before 'input' should be treated as above, and elements after should be treated as below.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
