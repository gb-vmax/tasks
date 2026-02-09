# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where blank lines in ESM blocks are not being handled correctly. When there's a blank line followed by more content in an import/export statement, the parser seems to be terminating the ESM block prematurely instead of continuing to parse it.

### Reproduction

```mdx
import { something } from 'somewhere'

export const config = {
  value: 'test'
}

# My Content
```

When parsing the above MDX content, the blank line between the import and export statements causes the parser to incorrectly process the ESM block. The export statement may not be recognized as part of the ESM block.

### Expected behavior

The parser should correctly handle blank lines within ESM blocks and continue parsing the entire block until it encounters actual content (like the heading in this case). Both the import and export statements should be processed as a single ESM block.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
