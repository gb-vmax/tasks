# Bug Report

### Describe the bug

The `bd` (border) prop on Box component is not working properly when passing a string value with border size, style, and color. The border doesn't render at all or renders incorrectly.

### Reproduction

```jsx
import { Box } from '@mantine/core';

function Demo() {
  return (
    <Box bd="1px solid red">
      Content here
    </Box>
  );
}
```

The border should be applied but nothing shows up. I've also tried with other variations:

```jsx
<Box bd="2px dashed blue">Content</Box>
<Box bd="3px solid var(--mantine-color-gray-5)">Content</Box>
```

None of them work. The border prop seems to be completely broken.

### Expected behavior

The border should be rendered with the specified size, style, and color. For example, `bd="1px solid red"` should create a 1px solid red border around the Box.

### System Info
- @mantine/core version: 7.x
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
