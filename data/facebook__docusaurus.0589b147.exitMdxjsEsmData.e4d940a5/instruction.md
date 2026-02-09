# Bug Report

### Describe the bug

I'm experiencing an issue with MDX ESM data handling where the parser seems to be processing ESM blocks incorrectly. The content inside ESM blocks (like import statements or export declarations) is not being parsed or rendered as expected.

### Reproduction

```mdx
---
import { Component } from './component'

export const metadata = {
  title: 'Test'
}
---

# My Document

<Component />
```

When parsing this MDX file, the ESM data (imports and exports) appears to be handled in the wrong order or context, causing the parser to fail or produce unexpected output.

### Expected behavior

The ESM blocks should be correctly parsed and the imports/exports should be available to the rest of the MDX content. The component should render properly and metadata should be accessible.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have started happening recently. The ESM blocks worked fine before, but now they're not being processed correctly during the parsing phase.

---
Repository: /testbed
