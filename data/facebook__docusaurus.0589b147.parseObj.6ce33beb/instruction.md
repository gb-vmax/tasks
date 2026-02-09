# Bug Report

### Describe the bug

I'm encountering a parsing error when trying to use MDX with object literals that have multiple properties. The parser seems to be incorrectly handling the comma separator between object properties.

### Reproduction

```jsx
export const config = {
  title: 'Hello',
  description: 'World'
}
```

When I try to parse MDX content with an object that has more than one property, I get a syntax error. Single-property objects work fine, but adding a second property causes the parser to fail.

### Expected behavior

The parser should correctly handle object literals with multiple properties separated by commas, just like standard JavaScript/JSX.

### Additional context

This seems to affect any object literal in MDX content - whether it's in exports, variable declarations, or JSX prop values. Objects with only one property parse without issues.

---
Repository: /testbed
