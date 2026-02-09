# Bug Report

### Describe the bug

I'm experiencing an issue where MDX import/export statements are not being processed correctly. It seems like the parser is not properly handling the module specifiers when there are previously defined ones.

### Reproduction

```mdx
import { ComponentA } from './components'
import { ComponentB } from './other'

export const metadata = {
  title: 'Test'
}

# My Document

<ComponentA />
<ComponentB />
```

When trying to parse MDX files with multiple import statements, the second and subsequent imports don't seem to be recognized properly. The first import works fine, but additional imports cause unexpected behavior.

### Expected behavior

All import/export statements should be parsed and processed correctly, regardless of how many module specifiers have been defined previously. Each import should be available for use in the MDX document.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
