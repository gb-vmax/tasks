# Bug Report

### Describe the bug

MDX ESM import/export statements are not being recognized when they start at the beginning of a line (column 1). The parser is rejecting valid ESM syntax that should be allowed.

### Reproduction

```mdx
import { something } from 'somewhere'

export const data = { value: 123 }

# My Content

This is my MDX content.
```

When trying to parse this MDX file, the import and export statements at the start of the file are not being processed correctly. The parser seems to be checking the column position incorrectly and rejecting statements that begin at column 1.

### Expected behavior

Import and export statements should be recognized and parsed correctly when they appear at the beginning of a line (column 1). Standard ESM syntax in MDX files should work as documented.

### Additional context

This affects any MDX file that has ESM imports/exports starting at column 1, which is the standard way to write these statements. The issue appears to be related to how the column position is being validated in the parser.

---
Repository: /testbed
