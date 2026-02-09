# Bug Report

### Describe the bug

I'm experiencing an issue with module exports after updating to the latest version. When trying to import named exports from certain modules, I'm getting `undefined` instead of the expected exported values.

### Reproduction

```js
// module.js
export const foo = 'bar';
export const baz = 'qux';

// consumer.js
import { foo, baz } from './module';

console.log(foo); // undefined
console.log(baz); // undefined
```

The exports are defined in the module but when importing them, they all come back as `undefined`. This seems to affect all named exports from the module.

### Expected behavior

Named exports should be properly accessible when imported. The values should match what was exported from the module.

### System Info
- Node version: 18.x
- Build tool: webpack/rollup

This wasn't happening in the previous version, so it seems like a recent regression. Any help would be appreciated!

---
Repository: /testbed
