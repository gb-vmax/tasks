# Bug Report

### Describe the bug

I'm encountering an issue with export default declarations where the variable name gets incorrectly overwritten when there are multiple references to it.

### Reproduction

```js
// input.js
export default function myFunction() {
  return 'test';
}

// another-file.js
import someAlias from './input.js';
```

When the exported function has an explicit name (`myFunction`) and is then imported with a different identifier (`someAlias`), the original function name seems to be getting replaced by the import alias. This affects the generated output and can break code that relies on the original function name.

### Expected behavior

The original name of the exported function should be preserved. Import aliases should not affect the name of the exported declaration itself. The function should maintain its `myFunction` name regardless of what identifier is used when importing it.

### Additional context

This seems to happen specifically with named function/class declarations that are exported as default. Anonymous exports don't seem to have this problem since they don't have an original name to preserve.

---
Repository: /testbed
