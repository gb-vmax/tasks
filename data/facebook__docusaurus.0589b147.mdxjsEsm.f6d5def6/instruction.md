# Bug Report

### Describe the bug

I'm experiencing an issue with MDX ESM import parsing where import statements seem to be processed incorrectly. When using named imports in MDX files, I'm getting unexpected behavior - it appears that the parser is either skipping specifiers or trying to access elements beyond the array bounds.

### Reproduction

```mdx
---
import { Component, AnotherComponent } from './my-components'
---

<Component />
<AnotherComponent />
```

When processing this MDX file, the import specifiers don't seem to be handled correctly. The parser appears to be missing one of the imported names or attempting to access an invalid array index.

### Expected behavior

All named imports should be correctly parsed and made available in the MDX document. Each specifier in the import statement should be processed exactly once.

### Additional context

This seems to affect how the ESM imports are tokenized and converted. The issue might be related to how events are sliced or how the specifiers array is iterated over during import declaration processing.

---
Repository: /testbed
