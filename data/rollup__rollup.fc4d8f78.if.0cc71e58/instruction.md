# Bug Report

### Describe the bug

When importing the same module with different import attributes, I'm not getting any warning messages. The bundler should warn about inconsistent import attributes when the same module is imported multiple times with different attributes, but it's staying silent.

### Reproduction

```js
// file1.js
import data from './data.json' with { type: 'json' };

// file2.js  
import data from './data.json' with { type: 'text' };
```

In this case, `data.json` is being imported with different attributes (`type: 'json'` vs `type: 'text'`), but no warning is logged even though the attributes are inconsistent.

### Expected behavior

The module loader should log a warning when the same module is imported with different/inconsistent import attributes across different files. This helps catch potential issues where developers might be importing the same resource with conflicting expectations.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
