# Bug Report

### Describe the bug

I'm encountering an issue with automatic semicolon insertion (ASI) in the MDX parser. It seems like the parser is incorrectly determining when semicolons can be automatically inserted, which is causing parsing errors in certain edge cases.

### Reproduction

When writing MDX code that relies on automatic semicolon insertion, the parser fails to correctly identify valid insertion points. This happens specifically when there's a closing brace followed by a line break.

For example:

```mdx
export const foo = {
  bar: 'baz'
}

console.log(foo)
```

The parser seems to be checking the wrong conditions or in the wrong order when determining if a semicolon can be inserted, leading to unexpected parsing behavior.

### Expected behavior

The parser should correctly identify when automatic semicolon insertion is allowed according to JavaScript/ECMAScript rules. Specifically, it should properly handle cases with closing braces and line breaks.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems like a regression as similar code was working in previous versions. Any help would be appreciated!

---
Repository: /testbed
