# Bug Report

### Describe the bug

I'm getting warnings about unknown options even though I'm only using valid configuration options. It seems like the validation is incorrectly flagging all valid options as unknown and displaying warnings for them.

### Reproduction

```js
import { rollup } from 'rollup';

const bundle = await rollup({
  input: 'src/main.js',
  plugins: [],
  external: ['lodash']
});
```

Even with completely valid options like `input`, `plugins`, and `external`, I'm seeing warnings in the console about unknown options being used.

### Expected behavior

No warnings should be displayed when using valid rollup configuration options. Warnings should only appear for actual unknown/invalid options that aren't part of the rollup API.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
