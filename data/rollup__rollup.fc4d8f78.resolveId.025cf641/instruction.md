# Bug Report

### Describe the bug

I'm experiencing an issue with module resolution where external module imports (like `import foo from 'lodash'`) are being incorrectly resolved as file paths instead of being treated as external dependencies. This causes the bundler to try to resolve them as local files, which fails.

### Reproduction

```js
// In a file with an importer path set
import something from 'external-package'
```

When the above import is processed, instead of treating `'external-package'` as an external module that should be skipped or handled separately, it attempts to resolve it as a relative file path. This breaks the build when using external dependencies that don't start with `'.'` or `'/'`.

### Expected behavior

External module imports (those that don't start with `'.'` or `'/'` and aren't absolute paths) should be handled correctly and not mistakenly resolved as local file paths. The module resolution should distinguish between:
- Local relative imports like `'./file.js'` or `'../utils.js'`
- External package imports like `'lodash'` or `'react'`

Currently it seems like the logic for determining what should be skipped vs resolved has been inverted.

### System Info
- rollup version: latest
- Node version: 18.x

---
Repository: /testbed
