# Bug Report

### Describe the bug

I'm experiencing an issue with MDX export handling where the generated code has incorrect export ordering and variable naming. When using `outputFormat: "program"`, the default export declaration appears in the wrong position in the output, and there's an off-by-one error in the `_exportAll` variable naming.

### Reproduction

```js
// Using @mdx-js/mdx with outputFormat: "program"
import { compile } from '@mdx-js/mdx'

const mdxSource = `
export { something } from './module'

# Hello World
`

const result = await compile(mdxSource, {
  outputFormat: 'program'
})

// The generated code has exports in wrong order
// and _exportAll variables are incorrectly numbered
console.log(result)
```

### Expected behavior

1. The default export declaration should appear after the function declaration in the output
2. The `_exportAll` variables should be numbered starting from 1 (e.g., `_exportAll1`, `_exportAll2`, etc.), not starting from 0

### Current behavior

- Default export appears before the function declaration
- `_exportAll` variables are numbered starting from 0 instead of 1

This seems to have broken the expected structure of the generated output and causes issues when the compiled MDX is consumed by other tools expecting a specific export order.

---
Repository: /testbed
