# Bug Report

### Describe the bug

When using `remarkStringify` with custom options, the options are being overridden by settings instead of the other way around. User-provided options should take precedence over default settings, but currently the settings are overwriting any custom options passed to the compiler.

### Reproduction

```js
const processor = unified()
  .use(remarkStringify, {
    bullet: '*',
    emphasis: '*'
  })
  .data('settings', {
    bullet: '-',
    emphasis: '_'
  });

const result = processor.stringify(tree);
// Expected: bullet='*', emphasis='*'
// Actual: bullet='-', emphasis='_'
```

### Expected behavior

Options passed directly to `remarkStringify` should have higher priority than settings configured via `data('settings')`. The user-provided options should not be overridden by the settings.

### Additional context

This affects any workflow where you need to pass specific formatting options to the stringify compiler while also having global settings configured. The current behavior makes it impossible to override settings on a per-call basis.

---
Repository: /testbed
