# Bug Report

### Describe the bug

I'm experiencing an issue with external variable access detection in my rollup bundle. It seems like the bundler is incorrectly determining when external variables have side effects, which is causing unexpected behavior in tree-shaking.

When accessing properties on external namespace imports, the bundler is not properly detecting whether these accesses should be considered as having effects. This leads to code being incorrectly included or excluded from the final bundle.

### Reproduction

```js
// external.js (external module)
export const foo = { bar: 'value' };
export default foo;

// main.js
import * as external from 'external';

// Accessing a property on the namespace
const result = external.foo.bar;
```

The bundler seems to be making incorrect decisions about whether these property accesses have side effects, particularly for namespace imports vs regular imports.

### Expected behavior

The bundler should correctly identify when accessing properties on external variables has effects based on:
- Whether it's a namespace import or regular import
- The depth of property access
- The type of interaction (access vs call vs assignment)

Property accesses on external variables should be evaluated consistently to ensure proper tree-shaking behavior.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
