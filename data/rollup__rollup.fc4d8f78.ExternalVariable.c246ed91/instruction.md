# Bug Report

### Describe the bug

I'm experiencing an issue with external module imports where the suggested name for the module is being set incorrectly. When importing default exports or namespace imports (`import * as foo`), the module name suggestion seems to be applied when it shouldn't be.

### Reproduction

```js
// In my bundle configuration
import defaultExport from 'external-module';
import * as namespace from 'another-module';

// The module name suggestion is being applied to these imports
// when it should only apply to named imports
```

After building, I noticed that the external module names are being suggested/renamed in cases where they shouldn't be - specifically for default and namespace imports. This appears to be the opposite of the expected behavior.

### Expected behavior

Module name suggestions should only be applied to **named imports**, not to default exports or namespace imports. Default and namespace imports should maintain their original naming without triggering the `suggestName` logic.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems like it might be a logic error in how external variables handle their references. The behavior changed recently and is affecting my build output.

---
Repository: /testbed
