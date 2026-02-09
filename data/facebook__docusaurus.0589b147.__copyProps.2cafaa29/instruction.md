# Bug Report

### Describe the bug

I'm experiencing an issue with module exports where properties are being incorrectly copied or excluded. When importing from MDX modules, some properties that should be available are missing, while properties that should be excluded are being included instead.

### Reproduction

```js
// When using MDX imports
import { SomeComponent, metadata } from './example.mdx'

// Expected: SomeComponent and metadata should be available
// Actual: Properties are not being exported correctly
```

The issue seems to affect how properties are enumerated and copied between objects. Properties that should be excluded from the export are appearing, while properties that should be included are being filtered out.

### Expected behavior

Module properties should be correctly exported based on their enumerable status. Properties marked for exclusion should not appear in the final export, and all other enumerable properties should be available.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
