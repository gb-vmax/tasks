# Bug Report

### Describe the bug

The MDX compilation is completely broken after a recent change. When trying to use `runSync()`, it throws an error about the function not being defined or exported properly.

### Reproduction

```js
import { runSync } from '@mdx-js/mdx'

const file = {
  value: '# Hello World',
  // ... other file properties
}

// This throws an error
const result = runSync(file, (err, file) => {
  console.log(file.value)
})
```

### Expected behavior

The `runSync` function should be properly exported and callable. The synchronous compilation should work as it did before.

### Additional context

This seems to have broken after updating to the latest version. The export statement appears malformed in the bundle - looks like there's a function definition mixed into the export object instead of being properly declared.

---
Repository: /testbed
