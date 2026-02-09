# Bug Report

### Describe the bug

I'm encountering an issue where MDX files with import/export statements are not being parsed correctly. The parser seems to be cutting off or truncating the tokenization logic, which causes imports and exports to fail silently or throw unexpected errors.

### Reproduction

```mdx
import { Component } from './Component'
export const metadata = { title: 'Example' }

# My Document

Content here...
```

When processing this MDX file, the import/export statements are not being handled properly. The parser appears to be incomplete and doesn't finish processing the module specifiers.

### Expected behavior

The MDX parser should correctly tokenize and parse import/export statements at the beginning of MDX files. Module specifiers should be properly extracted and the document should render without errors.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
