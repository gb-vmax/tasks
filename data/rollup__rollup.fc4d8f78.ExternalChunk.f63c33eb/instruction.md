# Bug Report

### Describe the bug

I'm experiencing an issue with external module path resolution. When using the `paths` option to customize external module paths, the custom paths are being ignored and the default normalized paths are used instead.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  external: ['my-external-lib'],
  output: {
    file: 'dist/bundle.js',
    format: 'es',
    paths: {
      'my-external-lib': 'custom/path/to/lib'
    }
  }
}
```

When bundling, the import statement in the output uses the normalized path instead of the custom path specified in the `paths` option:

```js
// Expected output:
import something from 'custom/path/to/lib';

// Actual output:
import something from '../node_modules/my-external-lib/index.js';
```

### Expected behavior

The `paths` option should take precedence over the default path normalization. Custom paths defined in the configuration should be used in the generated imports.

### Additional context

This seems to affect both object-based and function-based `paths` configurations. The custom paths are completely ignored regardless of how they're defined.

---
Repository: /testbed
