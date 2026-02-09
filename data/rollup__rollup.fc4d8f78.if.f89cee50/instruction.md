# Bug Report

### Describe the bug

I'm experiencing an issue with re-exports in ES modules. When trying to use `export * from 'module'` syntax, the re-export doesn't seem to be working correctly. The star export statement is not being generated in the output bundle.

### Reproduction

```js
// index.js
export * from './utils';

// utils.js
export const helper = () => 'test';
```

When bundling this code, the `export *` statement is missing from the final output. It seems like the bundler is not recognizing the star re-export pattern properly.

### Expected behavior

The bundled output should include the star export statement to re-export all named exports from the imported module. Something like:

```js
export * from './utils-abc123.js';
```

### Additional context

This worked fine in previous versions. The issue appeared recently and is breaking my library builds that rely on barrel exports.

---
Repository: /testbed
