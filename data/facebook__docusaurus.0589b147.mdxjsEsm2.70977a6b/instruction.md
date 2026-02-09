# Bug Report

### Describe the bug

I'm experiencing an issue with MDX compilation where ESM imports and exports are not being processed correctly. When I have ESM statements (like `import` or `export`) in my MDX files, they seem to disappear or not get included in the compiled output.

### Reproduction

```mdx
import { Component } from './Component'

export const metadata = {
  title: 'My Page'
}

# Hello World

<Component />
```

After compilation, the import and export statements are missing from the output, causing runtime errors when the component tries to reference `Component` or when other code tries to access the exported `metadata`.

### Expected behavior

ESM imports and exports should be preserved in the compiled output so that:
- Imported components/functions are available in the MDX content
- Exported values can be accessed by consuming code

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have started happening recently. The imports/exports work fine in regular JS/JSX files, just not in MDX.

---
Repository: /testbed
