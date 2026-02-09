# Bug Report

### Describe the bug

I'm experiencing an issue with MDX ESM imports where multi-line import statements are not being parsed correctly. The parser seems to exit the ESM data state prematurely, causing subsequent lines of the import to be treated as regular markdown content instead of part of the import statement.

### Reproduction

```mdx
import {
  ComponentA,
  ComponentB
} from './components'

# My Document

Content here...
```

When parsing this MDX file, the import statement gets broken up incorrectly. Only the first line is recognized as part of the import, and the remaining lines are treated as markdown text.

### Expected behavior

Multi-line import statements should be parsed as a single ESM block. The entire import declaration should be recognized and processed together, regardless of how many lines it spans.

### Additional context

This seems to affect any multi-line ESM syntax, including:
- Multi-line imports with destructuring
- Import statements split across multiple lines
- Export statements that span multiple lines

The parser appears to be exiting the ESM data state too early when encountering line breaks within the import/export block.

---
Repository: /testbed
