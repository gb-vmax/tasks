# Bug Report

### Describe the bug

I'm experiencing an issue with tree-shaking where the bundler seems to be getting stuck in an infinite loop or not properly completing the tree-shaking passes. After the recent update, my builds are hanging and never completing.

### Reproduction

```js
// Create a module with circular dependencies or complex export patterns
export { foo } from './module-a';
export { bar } from './module-b';

// module-a.js
import { bar } from './module-b';
export const foo = () => bar();

// module-b.js  
import { foo } from './module-a';
export const bar = () => foo();
```

When I try to bundle this code, the build process never completes. It seems like the tree-shaking logic is continuously requesting additional passes without ever settling.

### Expected behavior

The bundler should complete tree-shaking after a reasonable number of passes and finish the build process, even with circular dependencies or complex module graphs.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

This was working fine in the previous version, so I suspect something changed in how tree-shaking passes are being requested or tracked.

---
Repository: /testbed
