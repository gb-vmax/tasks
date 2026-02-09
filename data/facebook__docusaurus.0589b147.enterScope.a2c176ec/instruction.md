# Bug Report

### Describe the bug

I'm experiencing an issue with scope handling in the MDX parser. When entering a new scope, it seems like the scope stack isn't being managed correctly, causing variables and identifiers to not be properly tracked within nested scopes.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
export const outer = 'outer value'

{(() => {
  const inner = 'inner value'
  return <div>{inner}</div>
})()}
`

const result = await compile(mdxContent)
```

When compiling MDX content with nested scopes (like arrow functions or blocks), the parser doesn't correctly maintain the scope stack. Variables declared in inner scopes are not being resolved properly, or the scope hierarchy gets corrupted.

### Expected behavior

The scope stack should correctly track nested scopes so that:
1. Variables declared in inner scopes are properly recognized
2. Scope hierarchy is maintained throughout parsing
3. Variable lookups resolve to the correct scope level

### Additional context

This seems to affect any MDX content that uses nested JavaScript expressions or function scopes. The issue appears to be related to how scopes are pushed/managed during the parsing phase.

---
Repository: /testbed
