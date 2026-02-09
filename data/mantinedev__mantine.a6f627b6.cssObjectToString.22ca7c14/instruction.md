# Bug Report

### Describe the bug

The `cssObjectToString` function is generating incorrect CSS strings. When converting CSS objects to strings, properties with `undefined` values are being included in the output, and properties with actual values are not being converted properly.

### Reproduction

```js
import { cssObjectToString } from '@mantine/core';

const styles = {
  backgroundColor: 'red',
  color: 'blue',
  fontSize: undefined
};

const result = cssObjectToString(styles);
console.log(result);
// Output: "font-size:undefined;backgroundColor;color;"
// Expected: "background-color:red;color:blue;"
```

### Expected behavior

- Properties with `undefined` values should be excluded from the CSS string
- Property names should be converted from camelCase to kebab-case
- Property values should be included in the output
- The format should be `property-name:value;`

### System Info

- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
