# Bug Report

### Describe the bug

I'm experiencing an issue where modules that should be included in the bundle are being excluded during the tree-shaking process. After building my project, I'm getting runtime errors about missing modules that are actually imported and used.

### Reproduction

```js
// entry.js
import { usedFunction } from './module-a.js';

console.log(usedFunction());

// module-a.js
export function usedFunction() {
  return 'This should be included';
}
```

When I build this, the module gets incorrectly tree-shaken out even though it's clearly being used. The build completes without errors, but at runtime I get errors about the missing function.

### Expected behavior

Modules that are executed/imported should be included in the bundle during tree-shaking passes. The tree-shaking logic should only remove truly unused code, not code that's actually being referenced.

### Additional context

This seems to have started happening recently. The tree-shaking is being too aggressive and removing code that's actually needed. It's like the condition for determining whether a module should be included got inverted somehow.

---
Repository: /testbed
