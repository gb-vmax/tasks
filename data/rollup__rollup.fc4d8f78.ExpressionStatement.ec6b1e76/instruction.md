# Bug Report

### Describe the bug

I'm encountering an issue where custom directives at the module level are being stripped from the output bundle, but `'use strict'` directives are being kept instead. This is the opposite of what should happen - custom directives should be preserved while `'use strict'` should be removed (since modules are strict by default).

### Reproduction

```js
// input.js
'use asm';

export function calculate() {
  // some code
}
```

When bundling this code, the `'use asm'` directive gets removed from the output, even though it should be preserved at the module level. Meanwhile, if I use `'use strict'`, it incorrectly stays in the output.

### Expected behavior

- Custom directives like `'use asm'` should be included in the output when they appear at the module level
- The `'use strict'` directive should be excluded from the output (since ES modules are strict by default)
- A warning should be logged for directives other than `'use strict'` at the module level

### System Info

- Rollup version: latest
- Node version: 18.x

This seems like the logic for handling directives got inverted somehow. It's causing issues with asm.js modules that rely on the `'use asm'` directive being present.

---
Repository: /testbed
