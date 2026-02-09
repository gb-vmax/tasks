# Bug Report

### Describe the bug

I'm encountering an issue with namespace imports from external modules. When importing everything from an external module using `import * as something from 'external'`, the imported namespace is not being recognized correctly and behaves like a regular named import instead.

### Reproduction

```js
// In my rollup config
export default {
  input: 'src/index.js',
  external: ['external-lib'],
  output: {
    file: 'dist/bundle.js',
    format: 'esm'
  }
}

// In my source code (src/index.js)
import * as externalLib from 'external-lib';

// This should work but doesn't behave as expected
console.log(externalLib.someMethod());
```

The namespace import isn't being treated as a namespace - it seems to be handled as a regular named import. This breaks when trying to access properties on the imported namespace object.

### Expected behavior

When using `import * as name from 'external'`, the imported binding should be recognized as a namespace import, allowing access to all exported members of the external module through the namespace object.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
