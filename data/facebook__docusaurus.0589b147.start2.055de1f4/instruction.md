# Bug Report

### Describe the bug

MDX ESM imports/exports are not being recognized when they appear at the start of a file. The parser seems to be rejecting valid ESM syntax that should be allowed at column 1.

### Reproduction

```mdx
import { something } from 'somewhere'

# My Document

Content here...
```

When trying to parse this MDX file, the import statement at the beginning is not being processed correctly. The parser appears to be checking column position incorrectly and rejecting valid ESM blocks.

### Expected behavior

ESM import/export statements should be recognized and parsed when they start at column 1 (the beginning of a line). This is standard MDX behavior where imports and exports are allowed at the top level of the document.

### Additional context

This affects any MDX file that starts with an import or export statement. The issue seems related to how the column position is being validated in the ESM tokenizer.

---
Repository: /testbed
