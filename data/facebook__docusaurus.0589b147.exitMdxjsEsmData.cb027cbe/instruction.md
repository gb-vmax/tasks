# Bug Report

### Describe the bug

I'm experiencing an issue with MDX ESM data handling where the context (`this`) is being passed incorrectly in the `exitMdxjsEsmData` function. When processing MDX files with ESM imports/exports, the exit handler is being called with the wrong context, which causes the data processing to fail or behave unexpectedly.

### Reproduction

```js
// In an MDX file with ESM imports
import { something } from './module'

export const data = { foo: 'bar' }

# Content here
```

When this MDX is processed, the ESM data exit handler doesn't have access to the correct context, leading to errors or incorrect behavior during the transformation.

### Expected behavior

The `exitMdxjsEsmData` function should call the exit handler with the same context (`this`) as the enter handler, ensuring consistent access to the configuration and state throughout the ESM data processing lifecycle.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
