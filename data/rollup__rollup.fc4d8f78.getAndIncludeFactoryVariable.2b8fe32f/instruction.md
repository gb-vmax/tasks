# Bug Report

### Describe the bug

When using JSX with the `jsxImportSource` option and `preserve` mode, the wrong variable is being renamed during the bundling process. This causes the generated code to reference incorrect variable names, leading to runtime errors.

### Reproduction

```js
// Input code with nested JSX factory (e.g., React.createElement)
import React from 'react';

function Component() {
  return <div>Hello</div>;
}
```

With configuration:
```js
{
  jsx: {
    mode: 'preserve',
    importSource: 'react'
  }
}
```

### Expected behavior

The bundler should preserve the original variable names when in `preserve` mode and correctly handle the factory variable references. The generated code should maintain the correct references to the imported JSX factory.

### Actual behavior

The factory variable gets renamed incorrectly when it should be excluded from renaming. This results in the output code referencing a variable name that doesn't exist, causing "variable is not defined" errors at runtime.

### System Info

- Rollup version: latest
- Node version: 18.x

This seems to be affecting JSX transformations specifically when using nested factory names (like `React.createElement`) combined with preserve mode.

---
Repository: /testbed
