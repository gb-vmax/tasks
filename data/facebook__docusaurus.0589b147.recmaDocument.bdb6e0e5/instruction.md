# Bug Report

### Describe the bug

After a recent update, MDX documents are not rendering correctly. The content appears to be missing or duplicated in some cases, and there seem to be issues with exported identifiers not being handled properly.

### Reproduction

I'm working with MDX files that have the following structure:

```mdx
import { SomeComponent } from './components'

# My Document

Some content here

<SomeComponent />

export const metadata = { title: 'Test' }
```

When processing this file, the output is incorrect - sometimes the content is missing entirely, or the exports are not being recognized properly.

### Expected behavior

The MDX document should render with all content present and exports should be correctly identified and processed. The document structure should remain intact during the compilation process.

### Additional context

This seems to have started happening after updating the MDX compiler. The issue appears to be related to how the document structure is being analyzed and transformed during the compilation phase. Specifically:

1. Content may not appear when it should
2. Exported identifiers seem to be processed incorrectly

Has anyone else encountered similar issues with MDX document rendering?

---
Repository: /testbed
