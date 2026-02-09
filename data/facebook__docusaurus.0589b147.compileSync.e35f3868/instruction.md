# Bug Report

### Describe the bug

After a recent update, I'm getting a syntax error when trying to use the MDX compiler. It seems like there's an issue with the module exports - specifically the `compileSync` export appears to be malformed.

### Reproduction

```js
import { compileSync } from '@mdx-js/mdx';

const result = compileSync('# Hello World');
```

When running this code, I get a syntax error indicating that the export definition is invalid. The error occurs during module loading, before any actual compilation happens.

### Expected behavior

The `compileSync` function should be properly exported and callable without any syntax errors. It should compile MDX content synchronously and return the result.

### Additional context

Looking at the exports, it seems like the `compileSync` export definition got mixed up with some Sass compiler code? The export object shows `compile` is defined correctly, but `compileSync` has a completely different implementation that references `SassCompiler` which doesn't make sense for an MDX compiler.

This is blocking our build process since we rely on synchronous compilation in certain parts of our codebase.

---
Repository: /testbed
