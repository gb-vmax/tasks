# Bug Report

### Describe the bug

I'm experiencing an issue with external module imports where namespace imports are not being recognized correctly. When importing with `import * as foo from 'external-module'`, the module doesn't behave as a namespace and individual named exports seem to be treated as namespaces instead.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  external: ['external-lib'],
  output: {
    file: 'dist/bundle.js',
    format: 'esm'
  }
}

// src/index.js
import * as lib from 'external-lib';
import { namedExport } from 'external-lib';

console.log(lib);
console.log(namedExport);
```

### Expected behavior

- `import * as lib` should be treated as a namespace import
- `import { namedExport }` should be treated as a regular named import
- The bundled output should correctly distinguish between namespace and named imports

### Actual behavior

The namespace detection appears to be inverted - regular named imports are being treated as namespaces while the actual namespace import is not recognized as such.

### Environment

- Rollup version: latest
- Node version: 18.x
- OS: macOS

This seems to have started happening recently, possibly after a recent update. The generated code doesn't match what I'd expect for these import types.

---
Repository: /testbed
