# Bug Report

### Describe the bug
When parsing MDX files with ESM imports/exports, the parser is calling the data exit handler twice instead of calling enter then exit. This causes incorrect AST node processing for ESM data tokens.

### Reproduction
```js
// MDX file with ESM syntax
import { something } from 'module'

export const value = 42

# Content here
```

When this is parsed, the `exitMdxjsEsmData` function incorrectly calls `this.config.enter.data` first, then calls `this.config.exit.data` twice. This leads to an imbalanced enter/exit call sequence.

### Expected behavior
The function should call the enter handler once, then the exit handler once, maintaining proper token processing balance.

### System Info
- remark-mdx version: 3.0.0

---
Repository: /testbed
