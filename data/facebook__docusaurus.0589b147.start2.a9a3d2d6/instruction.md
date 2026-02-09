# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where blank lines after ESM imports are not being handled correctly. The parser seems to be processing blank lines in an unexpected way, causing the document structure to break.

### Reproduction

```mdx
import { something } from 'somewhere'

# My Heading

Content here
```

When parsing this MDX content, the blank line after the import statement causes incorrect tokenization. The parser appears to be treating the blank line improperly, which affects how subsequent content is processed.

### Expected behavior

The parser should correctly handle blank lines following ESM import statements. The blank line should be recognized and the parser should continue processing the rest of the document normally without any structural issues.

### Additional context

This seems to affect MDX documents that have:
1. ESM import statements at the top
2. One or more blank lines after the imports
3. Regular markdown content following

The issue appears to be related to how the `tokenizeNextBlank` function processes line endings and blank lines in the token stream.

---
Repository: /testbed
