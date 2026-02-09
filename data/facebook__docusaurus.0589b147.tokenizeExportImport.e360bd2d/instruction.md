# Bug Report

### Describe the bug

I'm encountering a parsing issue when using import/export statements in MDX files. It appears that the parser is failing to properly handle module specifiers, and the code execution is being cut off prematurely.

### Reproduction

```mdx
import { Component } from './component'

export const metadata = {
  title: 'Example'
}

# My Content

Some text here
```

When processing this MDX file, the parser seems to stop processing unexpectedly. The import/export statements aren't being handled correctly, and the content that should follow is not being parsed.

### Expected behavior

The parser should:
1. Correctly parse the import statement
2. Process the export declaration
3. Continue parsing the rest of the MDX content
4. Complete the full parsing cycle without truncation

### Additional context

This seems to affect files that have both import and export statements at the top. The issue appears to be related to how the parser handles the module specifiers and the AST body processing. The parsing just stops mid-way through processing the estree body.

---
Repository: /testbed
