# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where ESM imports and exports in MDX files are not being recognized correctly. When I try to use import/export statements in my MDX documents, they're being treated as regular expressions instead of ESM syntax.

### Reproduction

```mdx
export const metadata = {
  title: 'My Document'
}

import { Button } from './components'

# Hello World

<Button>Click me</Button>
```

When this MDX is parsed, the export and import statements don't work as expected. They seem to be processed incorrectly, causing the component imports to fail and metadata exports to not be available.

### Expected behavior

ESM import and export statements should be properly parsed and handled in MDX files. The imports should resolve correctly and exports should be accessible from the compiled output.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
