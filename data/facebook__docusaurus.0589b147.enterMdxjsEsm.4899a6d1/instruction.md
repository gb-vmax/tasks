# Bug Report

### Describe the bug

I'm encountering an issue with MDX ESM imports where they are being parsed incorrectly. It seems like ESM import/export statements in MDX files are being treated as flow expressions instead of proper ESM nodes.

### Reproduction

When I have an MDX file with ESM imports like:

```mdx
import { something } from 'somewhere'

# My Content

Regular markdown content here
```

The import statement is not being recognized as an `mdxjsEsm` node type. Instead, it appears to be processed as a different node type, which breaks the expected AST structure.

### Expected behavior

ESM import/export statements in MDX should be parsed as `mdxjsEsm` nodes in the syntax tree. The parser should correctly identify and handle these statements separately from other MDX expressions.

### Additional context

This affects any MDX file that uses ES module imports or exports at the top level. The issue impacts downstream tools that rely on the correct AST node types for processing MDX content.

---
Repository: /testbed
