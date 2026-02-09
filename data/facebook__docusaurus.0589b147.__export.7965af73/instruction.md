# Bug Report

### Describe the bug

I'm experiencing an issue where exported properties from MDX modules are not being properly exposed. It seems like the module exports are empty or undefined when they should contain the exported values.

### Reproduction

```js
// example.mdx
export const metadata = {
  title: 'Test Page',
  author: 'John Doe'
}

# Hello World

// consumer.js
import { metadata } from './example.mdx'

console.log(metadata) // undefined or empty object
```

When trying to access named exports from an MDX file, they're not available even though they're clearly defined in the source file.

### Expected behavior

The exported constants and functions from MDX files should be accessible when imported. In the example above, `metadata` should contain the object with title and author properties.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have started happening recently. The exports work fine in the actual MDX content rendering, but when trying to import them separately they're not available.

---
Repository: /testbed
