# Bug Report

### Describe the bug

I'm experiencing an issue with the vendored `mdast-util-to-string` module where properties are not being exported correctly. When trying to use exported functions from this module, I'm getting errors that the functions are undefined or not accessible.

### Reproduction

```js
// Attempting to import and use functions from the vendored module
import { toString } from './vendor/mdast-util-to-string@4.0.0.js'

const node = {
  type: 'text',
  value: 'hello world'
}

// This fails because toString is undefined
const result = toString(node)
```

### Expected behavior

The exported functions should be properly accessible and work as intended. The module should correctly export all its public API functions.

### System Info
- Jest version: latest
- Node version: 18.x

This seems to have broken recently, possibly after a vendor update. The module loads but the exports aren't working correctly.

---
Repository: /testbed
