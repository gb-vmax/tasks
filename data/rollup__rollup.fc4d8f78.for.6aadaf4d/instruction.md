# Bug Report

### Describe the bug

After a recent update, I'm seeing some strange behavior with module bundling. When I have modules with both static and dynamic imports, the generated bundle seems to have incorrect ordering of dependencies. The code executes but some modules are loaded in the wrong sequence, which breaks initialization order in certain cases.

### Reproduction

```js
// main.js
import { staticDep } from './static.js';
const dynamicDep = await import('./dynamic.js');

// static.js - needs to run first
export const staticDep = initializeConfig();

// dynamic.js - depends on config being initialized
export const dynamicDep = useConfig();
```

When bundling this, the dynamic import sometimes gets included before the static one in the final bundle, causing `useConfig()` to fail because the config hasn't been initialized yet.

### Expected behavior

Static dependencies should always be ordered before dynamic dependencies in the bundle. The execution order should respect the dependency graph properly, with static imports taking priority over dynamic ones.

### System Info
- Rollup version: latest
- Node version: 18.x

This is causing issues in production where module initialization order matters. Would appreciate any help debugging this!

---
Repository: /testbed
