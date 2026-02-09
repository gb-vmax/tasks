# Bug Report

### Describe the bug

When using the `unstyled` prop with component variants, the styling behavior is completely broken. It seems like variant classes are being applied when `unstyled={true}` is set, which is the opposite of what should happen. Additionally, the variant class name format appears to be incorrect.

### Reproduction

```jsx
import { Button } from '@mantine/core';

// This incorrectly applies variant styles even though unstyled is true
<Button variant="filled" unstyled={true}>
  Click me
</Button>

// This doesn't apply variant styles even though unstyled is false/undefined
<Button variant="filled" unstyled={false}>
  Click me
</Button>
```

### Expected behavior

- When `unstyled={true}`, variant classes should NOT be applied regardless of the variant prop
- When `unstyled={false}` or `unstyled` is not provided, variant classes should be applied normally
- The variant class name should follow the correct format: `${selector}--${variant}` not `${variant}--${selector}`

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
