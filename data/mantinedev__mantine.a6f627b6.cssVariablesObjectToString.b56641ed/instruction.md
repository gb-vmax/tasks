# Bug Report

### Describe the bug

CSS variables are not being rendered correctly when converted to string format. There's an extra space being added between variable declarations which breaks the CSS output.

### Reproduction

```js
import { cssVariablesObjectToString } from '@mantine/core';

const variables = {
  '--mantine-color-primary': '#228be6',
  '--mantine-spacing-md': '16px',
  '--mantine-font-size-sm': '14px'
};

const result = cssVariablesObjectToString(variables);
console.log(result);
// Output has spaces between declarations instead of being concatenated properly
```

### Expected behavior

The CSS variables should be concatenated without extra spaces between them. The output should be a valid CSS string that can be directly used in style attributes or style tags.

Expected output:
```
--mantine-color-primary: #228be6;--mantine-spacing-md: 16px;--mantine-font-size-sm: 14px;
```

Actual output seems to have spaces which might cause issues with CSS parsing in certain contexts.

### Additional context

This appears to affect how CSS variables are injected into components. The spacing issue could potentially cause problems with inline styles or when these variables are used in certain CSS contexts.

---
Repository: /testbed
