# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where `import` and `export` statements are not being recognized correctly. It seems like the parser is failing to properly identify these keywords at the start of lines.

### Reproduction

```mdx
import { Component } from './component'
export const meta = { title: 'Test' }

# My Document

Some content here.
```

When processing this MDX content, the import/export statements are not being parsed as ESM statements. Instead, they appear to be treated as regular text or rejected entirely.

### Expected behavior

The parser should correctly identify and process `import` and `export` keywords at the beginning of lines as valid ESM statements in MDX files. These statements should be extracted and handled separately from the markdown content.

### Additional context

This appears to be related to the tokenization logic for MDX ESM statements. The issue manifests when the parser encounters these keywords - they should trigger the appropriate parsing mode but currently don't seem to be working as expected.

---
Repository: /testbed
