# Bug Report

### Describe the bug

I'm experiencing an issue with default exports when there's only a single export in my module. The bundler seems to be ignoring the export entirely and not generating the correct output.

### Reproduction

```js
// module.js
export default function myFunction() {
  return 'hello';
}

// When bundled, the default export is not properly exposed
```

This also affects re-exported default imports:

```js
// re-export.js
export { default } from './external-module';

// The re-exported default is not being picked up correctly
```

### Expected behavior

When a module has a single default export, it should be properly included in the bundle and accessible to consumers. Re-exported defaults should also work as expected.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
