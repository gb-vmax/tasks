# Bug Report

### Describe the bug

I'm encountering a parsing issue when using import/export statements in MDX files. The parser seems to fail silently or produce unexpected results when processing module specifiers in certain scenarios.

### Reproduction

```mdx
import { something } from 'module'

export const value = 'test'

# Content here
```

When processing MDX files with import/export statements, especially when there are multiple imports or when using previously defined module specifiers, the parsing doesn't work as expected. The content after the import/export block may not be processed correctly.

### Expected behavior

Import and export statements should be parsed correctly and the module specifiers should be properly tracked and utilized throughout the parsing process. The parser should handle cases where module specifiers have been previously defined.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
