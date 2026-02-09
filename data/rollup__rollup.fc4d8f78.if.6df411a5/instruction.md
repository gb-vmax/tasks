# Bug Report

### Describe the bug

I'm experiencing an issue with tree-shaking behavior when `moduleSideEffects` is set to `'no-treeshake'`. It seems like the bundler is doing the opposite of what's expected - modules marked with `'no-treeshake'` are being tree-shaken, while other modules are being fully included in the bundle.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  output: {
    file: 'dist/bundle.js',
    format: 'esm'
  },
  treeshake: {
    moduleSideEffects: (id) => {
      // Mark specific module as no-treeshake
      if (id.includes('critical-module.js')) {
        return 'no-treeshake';
      }
      return true;
    }
  }
}

// critical-module.js
export const criticalFunction = () => {
  console.log('This should always be included');
};

// index.js
import { criticalFunction } from './critical-module.js';
// Function is imported but not used
```

### Expected behavior

When a module has `moduleSideEffects: 'no-treeshake'`, it should be fully included in the bundle without any tree-shaking applied to it. Instead, it appears the logic is inverted - modules with `'no-treeshake'` are being tree-shaken while other modules are being fully included.

The critical module should be completely preserved in the output bundle regardless of whether its exports are used or not.

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
