# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where whitespace handling in JSX tags seems to be broken. When using JSX expressions with whitespace (spaces, tabs, or line breaks), the parser appears to exit the whitespace state prematurely or in the wrong order, causing parsing errors or unexpected behavior.

### Reproduction

```mdx
<Component
  prop={
    value
  }
/>
```

Or with inline whitespace:

```mdx
<Component prop={ value } />
```

The parser fails to correctly handle the whitespace inside the JSX expression braces. It seems like the state machine for tracking whitespace is exiting states in an incorrect sequence.

### Expected behavior

The MDX parser should correctly handle whitespace (including line endings and unicode whitespace) inside JSX expressions without errors. The whitespace state should be exited only after properly consuming and processing the whitespace characters.

### Additional context

This appears to be related to the `esWhitespaceInside` function in the MDX tokenizer. The state transitions for handling whitespace inside ECMAScript/JSX expressions don't seem to be working as intended.

---
Repository: /testbed
