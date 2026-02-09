# Bug Report

### Describe the bug
When using `import` statements in MDX files, the parser fails to correctly recognize and process them. The import keyword detection appears broken, causing MDX content with import statements to not be parsed properly.

### Reproduction
```mdx
import { Component } from './Component'

# My Document

Some content here
```

The above MDX content fails to parse correctly. The `import` statement is not being recognized as valid ESM syntax.

### Expected behavior
Import statements should be properly detected and parsed when they appear at the beginning of MDX files. The parser should recognize "import" followed by a space as the start of an ESM import statement.

### Additional context
This seems to have broken recently. Export statements might still work, but import statements are definitely affected. The issue appears to be in the ESM tokenization logic where it checks for the import/export keywords.

---
Repository: /testbed
