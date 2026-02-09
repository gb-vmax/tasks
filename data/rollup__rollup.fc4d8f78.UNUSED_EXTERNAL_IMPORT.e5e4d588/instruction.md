# Bug Report

### Describe the bug

The warning message for unused external imports is displaying the module name twice in the output. When an external import is not used, the warning shows something like `"module-name""module-name"` instead of just `"module-name"`.

### Reproduction

1. Create a project with an external dependency
2. Import something from that external module but don't use it
3. Run the build
4. Check the warning output

Example:
```js
// In your code
import { something } from 'external-package';

// Don't use 'something' anywhere
```

The warning output shows:
```
Unused external imports
something imported from external module "external-package"external-package" but never used in...
```

### Expected behavior

The warning should display the external module name only once:
```
Unused external imports
something imported from external module "external-package" but never used in...
```

Also noticed that when there are multiple files with unused imports from the same external module, only the first file is shown in the warning message instead of listing all affected files.

---
Repository: /testbed
