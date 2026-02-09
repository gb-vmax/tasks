# Bug Report

### Describe the bug

When using JSX with a custom import source and a nested factory function (e.g., `React.createElement`), the import resolution is broken. The code tries to import the wrong specifier from the module.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.jsx',
  output: { file: 'dist/bundle.js' },
  jsx: {
    factory: 'React.createElement',
    importSource: 'react'
  }
}

// src/index.jsx
const App = () => <div>Hello</div>;
```

When the factory is specified as a nested name like `React.createElement` with an `importSource`, the bundler incorrectly tries to import the nested part (`createElement`) as the default export instead of importing the base name (`React`) as default.

### Expected behavior

With `factory: 'React.createElement'` and `importSource: 'react'`, it should generate:
```js
import React from 'react';
```

Instead, it's trying to import `createElement` directly which causes runtime errors since React doesn't export `createElement` as the default export.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
