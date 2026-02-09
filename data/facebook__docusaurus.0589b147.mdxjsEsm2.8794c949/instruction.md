# Bug Report

### Describe the bug

I'm experiencing an issue with MDX ESM imports where the code is throwing errors when processing MDX files with import/export statements. It seems like the parser is trying to access the wrong property on the estree object.

### Reproduction

```mdx
---
import { something } from './module'

export const config = {
  value: 'test'
}
---

# My Content

Some text here
```

When this MDX file is processed, I get errors related to the ESM handling. The imports and exports aren't being parsed correctly.

### Expected behavior

MDX files with ESM imports and exports should be processed without errors. The import/export statements should be extracted and handled properly by the parser.

### Additional context

This seems to have started happening recently. Previously, MDX files with imports/exports were working fine. Now they're causing the build to fail.

---
Repository: /testbed
