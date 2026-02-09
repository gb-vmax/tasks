# Bug Report

### Describe the bug

I'm encountering an issue with import statement generation in MDX files. When processing import declarations with multiple named imports, the code seems to hang or enter an infinite loop. The application becomes unresponsive when trying to parse certain import statements.

### Reproduction

```js
// This type of import statement causes the issue
import { ComponentA, ComponentB, ComponentC } from './components';

// Or with mixed import types
import DefaultComponent, { NamedExport } from './module';
```

When the MDX compiler tries to process files containing these import patterns, it stops responding. This happens specifically with imports that have named specifiers (the ones inside curly braces).

### Expected behavior

Import declarations should be processed correctly without hanging, and the generated output should properly handle all types of import specifiers including default imports, namespace imports, and named imports.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This is blocking our ability to use MDX files with standard ES6 import syntax. Any help would be appreciated!

---
Repository: /testbed
