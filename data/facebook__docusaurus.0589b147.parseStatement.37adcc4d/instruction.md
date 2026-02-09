# Bug Report

### Describe the bug

I'm experiencing an issue where import and export statements are being processed incorrectly. When I have an import statement in my MDX file, it's being treated as an export, and vice versa. This is causing syntax errors and unexpected behavior in my code.

### Reproduction

```js
// This import statement gets processed as an export
import { Component } from 'react'

// This export statement gets processed as an import
export const myVar = 'test'
```

When parsing MDX files with import/export statements, the parser seems to swap how it handles these keywords. Import declarations are being passed to the export handler and exports are being passed to the import handler.

### Expected behavior

Import statements should be parsed as imports and export statements should be parsed as exports. The parser should correctly identify the statement type and route it to the appropriate handler.

### Additional context

This appears to affect all MDX files that use ES6 module syntax. The issue manifests as parsing errors or incorrect AST generation when processing files with import/export statements.

---
Repository: /testbed
