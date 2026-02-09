# Bug Report

### Describe the bug

I'm experiencing an issue with MDX ESM parsing where the code doesn't properly handle end-of-file conditions in certain cases. When processing MDX files with ESM imports/exports, the parser seems to get stuck or not properly exit the data collection phase.

### Reproduction

```mdx
import { something } from 'module'

export const config = {
  value: 'test'
}

# Content here
```

When parsing MDX files with ESM blocks (imports/exports), the parser doesn't correctly recognize when it reaches the end of the ESM data section. This appears to happen specifically when there's no explicit newline or when the file ends immediately after an ESM statement.

### Expected behavior

The parser should properly exit the ESM data collection phase and transition to parsing the rest of the MDX content, regardless of whether there are trailing newlines or if the file ends abruptly.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
