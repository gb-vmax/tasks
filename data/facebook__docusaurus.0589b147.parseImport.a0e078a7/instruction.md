# Bug Report

### Describe the bug

I'm experiencing an issue with import statement parsing in MDX files. After a recent update, the parser seems to be consuming tokens in the wrong order, which causes import declarations to be parsed incorrectly.

### Reproduction

When I have MDX files with import statements like:

```js
import "some-module"
```

or

```js
import { Component } from "library"
```

The parser appears to be handling the tokens in an unexpected sequence. This affects how the import specifiers and source are being processed.

### Expected behavior

Import statements should be parsed correctly regardless of whether they are:
- Side-effect imports (e.g., `import "module"`)
- Named imports (e.g., `import { x } from "module"`)
- Default imports (e.g., `import x from "module"`)

The parser should properly handle the token sequence and semicolons for all import declaration types.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
