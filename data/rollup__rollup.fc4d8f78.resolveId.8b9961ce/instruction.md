# Bug Report

### Describe the bug

When using stdin input with custom module resolution, all module IDs are being returned instead of allowing the default resolution behavior to continue. This causes issues with normal module imports that should be handled by other plugins or the default resolver.

### Reproduction

```js
// rollup.config.js
import { stdinPlugin } from './cli/run/stdin';

export default {
  input: '-',
  plugins: [
    stdinPlugin('-')
  ],
  // ... other config
}
```

When trying to import regular modules in the stdin input:
```js
// stdin input
import something from 'external-package';
// This import fails to resolve correctly
```

### Expected behavior

The `resolveId` hook should only handle the stdin module itself and return `undefined` (or not return anything) for other module IDs, allowing them to be resolved by subsequent plugins or the default resolution mechanism.

Currently, non-stdin modules are not being resolved properly because the plugin is intercepting all resolution requests.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
