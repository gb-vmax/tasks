# Bug Report

### Describe the bug

I'm encountering an issue with MDX import statement parsing. When using simple import statements (without specifiers), the parser seems to be handling them incorrectly. The semicolon placement and specifier parsing appears to have changed behavior.

### Reproduction

```js
// Simple import without specifiers
import "some-module"

// This type of import is not being parsed correctly
```

When trying to parse MDX files with bare import statements (imports without named/default specifiers), the parser doesn't handle them properly anymore. The import source is being treated differently than expected.

### Expected behavior

Both types of imports should be parsed correctly:
- `import "module"` (bare import)
- `import { something } from "module"` (named import)

The parser should correctly identify when an import has no specifiers and handle the source accordingly.

### System Info
- remark-mdx version: 3.0.0

---
Repository: /testbed
