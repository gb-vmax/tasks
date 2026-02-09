# Bug Report

### Describe the bug

When I have a missing export warning, the first warning in the list is being skipped and not displayed. Only subsequent warnings are shown, which means if there's only one missing export, I don't see any output at all.

### Reproduction

Create a module with a missing export:

```js
// module.js
export const foo = 'bar';

// main.js
import { foo, baz } from './module.js'; // baz doesn't exist
```

When running the bundler, the missing export warning for `baz` is not displayed.

If you have multiple missing exports:

```js
// main.js
import { foo, baz, qux } from './module.js'; // baz and qux don't exist
```

Only the warning for `qux` is shown, but the first missing export (`baz`) is skipped.

### Expected behavior

All missing export warnings should be displayed, including the first one. The warning should show which binding is missing and from which module it's being imported.

### Additional context

This seems to have started recently. Previously all missing exports were being reported correctly.

---
Repository: /testbed
