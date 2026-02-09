# Bug Report

### CSS Variables rendering in wrong order

I'm experiencing an issue where CSS variables are being rendered incorrectly. The variable names and values appear to be swapped in the generated CSS.

### Reproduction
```js
import { MantineProvider } from '@mantine/core';

const cssVars = {
  '--my-color': 'red',
  '--my-size': '16px'
};

// Expected output: "--my-color: red; --my-size: 16px;"
// Actual output: "red: --my-color; 16px: --my-size;"
```

When I inspect the DOM, the CSS custom properties are completely backwards - the values are where the property names should be and vice versa. This breaks all styling that depends on these variables.

### Expected behavior
CSS variables should be formatted as `propertyName: value;` not `value: propertyName;`

### Additional context
This seems to affect all CSS variables passed through MantineProvider. The variables are being written to the DOM but in an invalid format that browsers can't parse.

---
Repository: /testbed
