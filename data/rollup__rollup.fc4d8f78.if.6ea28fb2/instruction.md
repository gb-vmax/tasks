# Bug Report

### Describe the bug

I'm experiencing an issue with default export imports where the interop helpers are being applied incorrectly. It seems like the logic for determining when to add default interop helpers has been inverted - non-default exports are being treated as if they need default interop helpers, while actual default exports are not getting the correct treatment.

### Reproduction

```js
// external.js
export default function myFunction() {
  return 'default export';
}

export function namedExport() {
  return 'named export';
}

// main.js
import myDefault from './external.js';
import { namedExport } from './external.js';

console.log(myDefault());
console.log(namedExport());
```

When bundling this code, the default import doesn't get the proper interop helper applied, but named exports incorrectly receive default interop handling.

### Expected behavior

Default exports should receive default interop helpers when needed based on the interop type, while named exports should not. The condition should check if `variable.name === 'default'` to apply default interop helpers, not the opposite.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
