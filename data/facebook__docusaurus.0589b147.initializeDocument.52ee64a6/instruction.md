# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where container states aren't being properly closed in certain scenarios. When working with nested markdown structures (like lists or blockquotes), the parser seems to be exiting containers incorrectly, which leads to malformed output or unexpected parsing behavior.

### Reproduction

```js
const markdown = `
> Quote level 1
> > Quote level 2
> > Still level 2
> Back to level 1
`;

const result = parse(markdown);
// The nested quote structure is not preserved correctly
```

This also happens with nested lists and other container-like markdown elements. The issue appears when transitioning between different nesting levels - the parser doesn't properly close the container states.

### Expected behavior

The parser should correctly handle nested container structures and maintain proper nesting levels throughout the document. When exiting from a nested container back to a parent container, the state should be properly preserved.

### Additional context

This seems to affect documents with multiple levels of nesting. Simple single-level containers work fine, but once you have 2+ levels of nesting and transition between them, the parsing gets confused.

---
Repository: /testbed
