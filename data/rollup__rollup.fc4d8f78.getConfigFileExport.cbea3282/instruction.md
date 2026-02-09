# Bug Report

### Describe the bug

When using rollup in watch mode, configuration file warnings are not being displayed. The warning handler appears to be removed too early in the config loading process, which prevents any warnings from the imported config file from being captured and shown to the user.

### Reproduction

1. Create a rollup config file that triggers a warning during import (e.g., using deprecated Node.js APIs or modules with warnings)
2. Run rollup in watch mode
3. Observe that warnings that should appear are silently suppressed

Example config that should trigger warnings:
```js
// rollup.config.js
import { someDeprecatedAPI } from 'some-module';

export default {
  input: 'src/index.js',
  output: {
    file: 'dist/bundle.js',
    format: 'esm'
  }
};
```

### Expected behavior

Warnings emitted during config file loading should be displayed to the user, regardless of whether rollup is running in watch mode or not. The warning handler should remain active until after the config file has been fully imported.

### System Info
- Rollup version: latest
- Node.js version: 18.x
- OS: Any

---
Repository: /testbed
