# Bug Report

### Describe the bug

I'm encountering an issue with the MDX parser configuration validation. When I provide a valid `acorn` instance with both `parse` and `parseExpressionAt` methods, the parser throws an error claiming that a proper `acorn` instance is expected. This is preventing me from using custom acorn configurations.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'
import * as acorn from 'acorn'

const mdxSource = `# Hello World`

// This throws an error even though acorn is valid
const result = await compile(mdxSource, {
  acorn: acorn,
  acornOptions: {
    ecmaVersion: 2020
  }
})
```

The error message says:
```
Expected a proper `acorn` instance passed in as `options.acorn`
```

But I'm passing a valid acorn instance that has both required methods.

### Expected behavior

The parser should accept a valid `acorn` instance that has `parse` and `parseExpressionAt` methods without throwing an error. The compilation should proceed normally with the custom acorn configuration.

### Additional context

This seems to have started recently. I'm using a standard acorn import and the instance definitely has the required methods. Also noticed that if I provide `acornOptions` without `addResult`, I get another error about expecting an acorn instance, which seems inconsistent.

---
Repository: /testbed
