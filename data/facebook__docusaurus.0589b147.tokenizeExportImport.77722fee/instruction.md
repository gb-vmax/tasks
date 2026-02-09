# Bug Report

### Describe the bug

I'm experiencing an issue with MDX ESM import/export parsing where the code appears to be truncated or incomplete. When processing MDX files with import or export statements, the parsing seems to fail silently or behave unexpectedly.

### Reproduction

```mdx
import { something } from 'module'

# My Content

Some text here
```

When trying to parse this MDX content, the import statement doesn't seem to be processed correctly. The issue appears to be related to how module specifiers are being handled internally.

### Expected behavior

Import and export statements in MDX files should be parsed correctly and the module specifiers should be properly tracked. The parser should complete its processing without any issues.

### System Info

- @mdx-js/mdx version: 3.0.0
- Node version: Latest LTS

### Additional context

This seems to have started happening recently. The parsing logic for ESM imports/exports might be incomplete as the tokenization process doesn't seem to finish properly.

---
Repository: /testbed
