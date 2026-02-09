# Bug Report

### Describe the bug

MDX ESM imports/exports are not being recognized when they appear at the start of a line (column 1). The parser seems to be rejecting valid ESM syntax that should be accepted.

### Reproduction

```mdx
import { something } from 'somewhere'

export const data = { test: true }

# My Content

Regular markdown content here.
```

When parsing the above MDX content, the ESM import and export statements at the beginning of the file are not being processed correctly. They should be valid MDX ESM blocks but are being rejected by the parser.

### Expected behavior

ESM import/export statements that start at column 1 (the beginning of a line) should be properly parsed and recognized as valid MDX ESM syntax. This is standard MDX behavior where imports and exports can appear at the top of the file.

### Additional context

This appears to affect any ESM statement that starts at the very beginning of a line. Moving the statement to have leading whitespace might work around the issue, but that's not valid ESM syntax and breaks the expected MDX format.

---
Repository: /testbed
