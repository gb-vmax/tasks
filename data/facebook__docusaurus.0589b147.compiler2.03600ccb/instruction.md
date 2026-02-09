# Bug Report

### Describe the bug

When using the remark stringify compiler, custom settings passed via options are being overridden by settings from `self.data("settings")`. This means that any configuration I explicitly pass to `remarkStringify()` gets ignored if there are also settings stored in the data object.

### Reproduction

```js
const processor = unified()
  .use(remarkParse)
  .use(remarkStringify, {
    bullet: '*',
    emphasis: '*'
  });

// If self.data("settings") contains { bullet: '-' }
// The output will use '-' instead of '*' for bullets
// even though I explicitly passed bullet: '*' in options
```

### Expected behavior

Options passed directly to `remarkStringify()` should take precedence over settings from `self.data("settings")`. When I explicitly configure the compiler with specific options, those should be respected and not overridden by data settings.

Currently the spread order is:
```js
{
  ...self.data("settings"),
  ...options
}
```

This means `self.data("settings")` values override my explicit `options`, which is counterintuitive.

### Additional context

This affects any scenario where plugins or other parts of the system set default settings via `self.data("settings")`, making it impossible to override those defaults when calling `remarkStringify()` with custom options.

---
Repository: /testbed
