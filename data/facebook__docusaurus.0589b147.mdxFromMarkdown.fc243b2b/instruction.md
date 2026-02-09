# Bug Report

### Describe the bug

I'm experiencing an issue where MDX files with ESM imports/exports are not being parsed correctly. The imports and exports seem to be ignored or not processed, causing the MDX compilation to fail or produce unexpected output.

### Reproduction

```js
// test.mdx
import { Component } from './Component'

export const metadata = {
  title: 'Test'
}

# Hello World

<Component />
```

When trying to compile this MDX file, the ESM import and export statements are not being handled properly. The component doesn't get imported and the metadata export is not available.

### Expected behavior

ESM imports and exports should be properly parsed and included in the compiled output. Both import statements and export declarations at the top of MDX files should work as documented.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
