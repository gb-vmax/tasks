# Bug Report

### Describe the bug

After a recent update, I'm getting a syntax error when trying to use the VCS utilities. It looks like there's a duplicate function definition in the `util.ts` file that's preventing the code from compiling.

### Reproduction

When importing or using functions from `packages/insomnia/src/sync/vcs/util.ts`, the module fails to load with a syntax error about duplicate function declarations.

```js
import { generateStateMap } from './sync/vcs/util';

// Attempting to use the function results in a compilation error
const stateMap = generateStateMap(someState);
```

### Expected behavior

The `generateStateMap` function should be defined once and work correctly when generating a state map from snapshot state.

### System Info
- Insomnia version: latest
- Node version: 18.x

This seems to have been introduced in a recent commit. The file appears to have multiple definitions of the same function which causes the build to fail.

---
Repository: /testbed
