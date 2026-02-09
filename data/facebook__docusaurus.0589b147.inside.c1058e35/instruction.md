# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where inline ESM imports/exports are not being processed correctly. It seems like the parser is exiting the ESM data state prematurely after consuming each character instead of continuing to parse the full ESM statement.

### Reproduction

```mdx
import { something } from 'module'

# My Document

Some content here
```

When parsing this MDX content, the ESM import statement gets incorrectly tokenized. The parser appears to be treating each character as a separate token boundary rather than continuing to consume characters until reaching a line ending.

### Expected behavior

The parser should consume the entire ESM statement (import/export) as a continuous data block until it encounters a line ending or end of file. Each character within the statement should be consumed without exiting the ESM data state.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

This is causing MDX files with ESM imports/exports to fail parsing or produce unexpected output. Any help would be appreciated!

---
Repository: /testbed
