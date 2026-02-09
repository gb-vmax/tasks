# Bug Report

### Describe the bug

I'm encountering a parsing issue with JSX text content in MDX files. It seems like JSX text is not being parsed correctly - the parser is treating non-text tokens as text and failing to properly identify actual JSX text nodes.

### Reproduction

When trying to parse an MDX file with JSX elements containing text:

```jsx
<div>
  Hello World
</div>
```

The text content "Hello World" is not being recognized properly. Instead, the parser appears to be misidentifying what should be treated as JSX text.

### Expected behavior

JSX text content should be correctly parsed and recognized when it appears inside JSX elements. The parser should distinguish between JSX text tokens and other token types.

### Additional context

This appears to be related to the token type checking logic in the expression atom parser. The condition for identifying JSX text seems inverted - it's checking for the wrong condition when determining whether to parse text content.

---
Repository: /testbed
