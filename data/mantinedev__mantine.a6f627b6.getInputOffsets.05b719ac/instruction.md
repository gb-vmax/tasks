# Bug Report

### Describe the bug
The `InputWrapper` component is not calculating the correct offset when the description is positioned above the input. The offset logic seems to be checking the wrong part of the `inputWrapperOrder` array, causing the description spacing to be applied incorrectly.

### Reproduction
```jsx
import { Input } from '@mantine/core';

function Demo() {
  return (
    <Input.Wrapper
      label="Label"
      description="This is a description"
      inputWrapperOrder={['label', 'description', 'input', 'error']}
    >
      <Input />
    </Input.Wrapper>
  );
}
```

When the description is placed above the input (between label and input), the top offset is not being applied correctly. The spacing between the description and input doesn't match the expected behavior.

### Expected behavior
When `description` appears in the `inputWrapperOrder` array before `'input'`, the appropriate top offset should be applied to create proper spacing. Currently it seems like the offset calculation is looking at the wrong section of the order array.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
