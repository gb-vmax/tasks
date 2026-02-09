# Bug Report

### Describe the bug

The `camelToKebabCase` utility function is not converting camelCase strings correctly. It only converts the first uppercase letter and places the dash in the wrong position.

### Reproduction

```js
import { camelToKebabCase } from '@mantine/core';

// Expected: 'background-color'
// Actual: 'background-color'
console.log(camelToKebabCase('backgroundColor'));

// Expected: 'my-custom-property'
// Actual: 'mycustom-property'
console.log(camelToKebabCase('myCustomProperty'));

// Expected: 'border-top-left-radius'
// Actual: 'bordertopleft-radius'
console.log(camelToKebabCase('borderTopLeftRadius'));
```

### Expected behavior

The function should convert all uppercase letters to lowercase and prepend them with a dash. For example:
- `backgroundColor` → `background-color`
- `myCustomProperty` → `my-custom-property`
- `borderTopLeftRadius` → `border-top-left-radius`

Currently it only processes the first capital letter and puts the dash after instead of before.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
