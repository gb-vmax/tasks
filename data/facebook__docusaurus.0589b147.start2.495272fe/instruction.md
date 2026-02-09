# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where blank lines after ESM imports are not being handled correctly. The parser seems to be accepting invalid syntax or rejecting valid syntax when there are blank lines following import statements.

### Reproduction

```mdx
import { Component } from './component'

export const metadata = { title: 'Test' }

# Heading

Content here
```

When parsing this MDX content, the blank line handling appears to be inverted - it's treating valid blank lines as errors or vice versa. The parser behavior around line endings after ESM blocks seems inconsistent.

### Expected behavior

The parser should correctly handle blank lines after ESM import/export statements. Valid MDX with proper spacing should parse without issues, and invalid syntax should be properly rejected.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
