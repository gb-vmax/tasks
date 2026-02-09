# Bug Report

### Describe the bug

I'm encountering an issue with variable scope resolution in MDX files. It seems like variables that should be recognized as in-scope are being treated as undefined or out-of-scope, causing unexpected behavior.

### Reproduction

```jsx
import { SomeComponent } from './components'

export const myVariable = 'test'

function MyFunction() {
  const localVar = 'local'
  
  return (
    <div>
      {/* This should work but throws an error about undefined variable */}
      {localVar}
    </div>
  )
}
```

When using locally scoped variables or trying to reference variables defined in the same file, they're not being recognized properly. This affects both function-scoped variables and module-level exports.

### Expected behavior

Variables defined within the same scope (function scope, module scope, etc.) should be accessible and not throw undefined variable errors. The scope chain should be traversed correctly to find variable declarations.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have started happening recently. Not sure if it's related to a recent change in how scope resolution works.

---
Repository: /testbed
