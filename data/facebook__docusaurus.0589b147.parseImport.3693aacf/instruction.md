# Bug Report

### Describe the bug

After a recent update, import statements in MDX files are being parsed incorrectly. The parser seems to be checking for the "from" keyword at the wrong position in the import statement, causing valid import syntax to fail.

### Reproduction

```js
// This import statement fails to parse correctly
import { Component } from 'library'

// Also having issues with simple string imports
import 'styles.css'
```

When processing MDX files with these import statements, the parser throws errors or produces unexpected results. The issue appears to be related to how the parser handles the "from" contextual keyword and semicolons in import declarations.

### Expected behavior

Standard ES6 import syntax should be parsed correctly:
- `import 'module'` - side-effect imports
- `import { named } from 'module'` - named imports
- `import Default from 'module'` - default imports

All of these should work without errors in MDX files.

### System Info
- @mdx-js/mdx version: 3.0.0
- Parser: acorn-based

This seems like a regression as these imports were working fine in the previous version.

---
Repository: /testbed
