# Bug Report

### Describe the bug

I'm encountering an issue with the config file loader where relative imports are being incorrectly treated as external dependencies. When I try to import local modules using relative paths (like `./utils` or `../helpers`), they're not being resolved properly and the build fails.

### Reproduction

```js
// rollup.config.js
import { someHelper } from './helpers.js';
import { anotherUtil } from '../utils/index.js';

export default {
  input: 'src/index.js',
  output: {
    file: 'dist/bundle.js',
    format: 'esm'
  }
};
```

When running the build with this config, I get errors about unresolved imports even though the files exist at those paths.

### Expected behavior

Relative imports (starting with `./` or `../`) should be resolved correctly and not marked as external. Only actual external packages (like `lodash` or `react`) should be treated as external.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

This seems to have started happening recently, possibly after a recent update. The config worked fine before.

---
Repository: /testbed
