# Bug Report

### Describe the bug

I'm getting warnings for every single option I pass to rollup, even when they're valid. It seems like the option validation is broken and it's treating all options as unknown.

### Reproduction

```js
import { rollup } from 'rollup';

const bundle = await rollup({
  input: 'src/main.js',
  plugins: []
});

// Console shows warnings like:
// (!) Unknown input options: input, plugins. Allowed options: ...
```

Even basic options like `input` and `plugins` are being flagged as unknown, which doesn't make sense.

### Expected behavior

Valid rollup options should not trigger unknown option warnings. Only options that are actually invalid or misspelled should generate warnings.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
