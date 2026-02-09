# Bug Report

### Describe the bug

I'm experiencing an issue with external module path resolution. When using the `paths` option with external modules, the generated import paths are incorrect. The imports are pointing to the wrong locations, which breaks the build output.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/main.js',
  external: ['some-external-lib'],
  output: {
    file: 'dist/bundle.js',
    format: 'es',
    paths: (id) => {
      if (id === 'some-external-lib') {
        return './custom/path/to/lib';
      }
    }
  }
}
```

When the bundle is generated, the import path for `some-external-lib` is not using the custom path returned by the `paths` function. Instead, it's using the original module ID.

### Expected behavior

The generated bundle should use the custom path specified in the `paths` function:
```js
import something from './custom/path/to/lib';
```

But instead it's generating:
```js
import something from 'some-external-lib';
```

This seems to have started happening recently. The `paths` function is being called correctly, but its return value is being ignored in certain cases.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
