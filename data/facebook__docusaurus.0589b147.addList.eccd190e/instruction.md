# Bug Report

### Describe the bug

I'm encountering an issue when using MDX with an empty plugin array. After a recent update, passing an empty array `[]` to the plugins configuration throws an unexpected `TypeError` saying "Expected a list of plugins, not `[]`".

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

// This now throws an error
const result = await compile('# Hello', {
  remarkPlugins: []
})
```

The error message is:
```
TypeError: Expected a list of plugins, not ``
```

### Expected behavior

An empty plugin array should be valid and simply mean "no plugins". This was working fine before and is a common pattern when you want to conditionally add plugins or start with a base configuration.

Many users pass empty arrays as default values or when no plugins are needed, so this breaks existing code.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
