# Bug Report

### Describe the bug

MDX ESM imports/exports are not being recognized when placed at the beginning of a line. It seems like there's an issue with column position checking that's preventing valid ESM syntax from being parsed correctly.

### Reproduction

```mdx
import { something } from 'somewhere'

export const data = { value: 42 }

# My Content

This should work but the imports/exports above are not being processed.
```

When I try to use MDX with ESM imports or exports starting at column 1 (the beginning of the line), they're not being recognized as valid ESM syntax. The parser seems to be rejecting them even though they should be valid.

### Expected behavior

ESM imports and exports should be recognized and processed when they appear at the start of a line (column 1). This is standard MDX behavior and how it worked in previous versions.

### Additional context

This appears to affect all ESM syntax (import/export statements) that starts at the beginning of a line. The content is being treated as regular markdown instead of being parsed as ESM.

---
Repository: /testbed
