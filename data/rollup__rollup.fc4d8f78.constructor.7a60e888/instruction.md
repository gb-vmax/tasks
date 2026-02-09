# Bug Report

### Describe the bug

When using plugins in rollup, the plugin execution order seems to be reversed from what's expected. Plugins that should run first are executing after plugins that should run later, causing hooks to fire in the wrong sequence.

This is particularly noticeable when using output plugins together with input plugins - the output plugins appear to be executing before the input plugins, which breaks the expected plugin lifecycle.

### Reproduction

```js
import { rollup } from 'rollup';

const inputPlugin = {
  name: 'input-plugin',
  buildStart() {
    console.log('Input plugin buildStart');
  }
};

const outputPlugin = {
  name: 'output-plugin',
  renderStart() {
    console.log('Output plugin renderStart');
  }
};

const build = await rollup({
  input: 'src/index.js',
  plugins: [inputPlugin]
});

await build.generate({
  format: 'es',
  plugins: [outputPlugin]
});
```

Expected order:
1. Input plugins execute first
2. Output plugins execute after

Actual behavior:
The plugins seem to be executing in reversed order, with output plugins potentially running before input plugins in the internal plugin array.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
