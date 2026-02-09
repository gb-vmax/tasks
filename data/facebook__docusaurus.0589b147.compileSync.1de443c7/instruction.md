# Bug Report

### Describe the bug

After a recent update, I'm getting syntax errors when trying to use the MDX compiler. It looks like there's a problem with the module exports - specifically the `compileSync` export seems to be malformed.

### Reproduction

```js
import { compileSync } from '@mdx-js/mdx'

const result = compileSync('# Hello World')
```

When running this code, I get a syntax error about unexpected token or invalid export syntax. The import statement itself fails to load the module properly.

### Expected behavior

The `compileSync` function should be properly exported and available for import. The module should load without any syntax errors.

### Additional context

This appears to have started happening recently. The other exports like `compile`, `evaluate`, etc. seem to work fine, but `compileSync` specifically is broken. Looks like there might be an issue with how the exports are defined in the bundled vendor file.

---
Repository: /testbed
