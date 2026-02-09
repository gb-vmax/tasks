# Bug Report

### Describe the bug

MDX ESM imports are being rejected when they appear at the start of a line (column 1). The parser seems to be incorrectly checking column positions and preventing valid ESM statements from being parsed.

### Reproduction

```mdx
import { something } from 'module'

# My Document

Content here...
```

When trying to parse this MDX content, the import statement at column 1 gets rejected even though it's valid MDX syntax. ESM imports should be allowed at the beginning of the file.

### Expected behavior

ESM import/export statements should be recognized and parsed correctly when they start at column 1. The column check should allow statements that begin at the start of a line.

### Additional context

This appears to affect all ESM statements (import, export, etc.) that are positioned at the beginning of a line. Moving them to start at column 2 or later might work around the issue, but that's not valid JavaScript/MDX syntax.

---
Repository: /testbed
