# Bug Report

### Describe the bug

I'm experiencing an issue with MDX ESM block parsing where the content inside ESM blocks is not being processed correctly. It seems like the parser is handling line breaks and continuation logic in an unexpected way, causing ESM import/export statements to fail or behave strangely.

### Reproduction

```mdx
import { Something } from 'somewhere'

export const config = {
  title: 'My Page'
}

# Content here
```

When parsing this MDX file, the ESM blocks (import/export statements) don't seem to be recognized properly. The parser appears to be treating line endings differently than expected, which breaks the ESM block detection.

### Expected behavior

ESM import and export statements at the top of MDX files should be parsed correctly and treated as valid ESM blocks. The parser should properly handle line endings within these blocks and distinguish between actual content and ESM code.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
