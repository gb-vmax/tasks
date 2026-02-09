# Bug Report

### Describe the bug

I'm encountering an issue with MDX expression formatting where parentheses are being added incorrectly around expressions. It seems like expressions that don't need parentheses are getting wrapped in them, while expressions that should be parenthesized are not.

### Reproduction

When using MDX with JavaScript expressions, I'm seeing unexpected parentheses in the generated output:

```mdx
{someVariable}
{a + b}
{foo.bar}
```

These expressions are being wrapped in parentheses when they shouldn't be, resulting in output like:

```js
(someVariable)
(a + b)
(foo.bar)
```

This is causing issues with the generated code and making the output unnecessarily verbose.

### Expected behavior

Expressions should only be wrapped in parentheses when they actually need them based on operator precedence and context. Simple variable references and straightforward expressions shouldn't have extra parentheses added.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
