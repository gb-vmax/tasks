# Bug Report

### Describe the bug

When passing CSS properties with `undefined` values to inline styles, the properties are incorrectly included in the generated CSS string instead of being filtered out. This results in invalid CSS being rendered with `undefined` appearing in the style attribute.

### Reproduction

```jsx
import { cssObjectToString } from '@mantine/core';

const styles = {
  color: 'red',
  backgroundColor: undefined,
  fontSize: '16px'
};

const result = cssObjectToString(styles);
console.log(result);
// Expected: "color:red;font-size:16px;"
// Actual: "background-color:undefined;color:red;font-size:16px;"
```

The function is now including properties with `undefined` values in the output string, which creates invalid CSS. Additionally, there seems to be an issue with the trimming behavior - only leading whitespace is being removed instead of all surrounding whitespace.

### Expected behavior

Properties with `undefined` values should be excluded from the CSS string output entirely. The function should only include properties that have defined values.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: All browsers affected

---
Repository: /testbed
