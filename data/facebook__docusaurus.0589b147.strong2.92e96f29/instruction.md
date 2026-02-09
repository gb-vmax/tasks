# Bug Report

### Describe the bug
When using the `strong` element in MDX, it's generating incorrect output. The strong formatting appears to be broken and not rendering as expected.

### Reproduction
```jsx
import { compile } from '@mdx-js/mdx'

const mdx = `
This is **bold text** that should be strong.
`

const result = await compile(mdx)
```

When I try to use bold/strong text in my MDX files, the output doesn't seem to be correct. The strong elements aren't being processed properly.

### Expected behavior
Bold text wrapped in `**` should render as strong/bold elements in the output. The strong element should have the correct type and properly initialized children array.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
