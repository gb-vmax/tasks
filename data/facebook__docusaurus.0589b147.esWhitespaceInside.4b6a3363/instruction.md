# Bug Report

### Describe the bug

I'm experiencing an issue with whitespace handling in MDX JSX tags. When there are multiple spaces or whitespace characters inside JSX expressions, the parser seems to be consuming them incorrectly, leading to unexpected behavior or parsing errors.

### Reproduction

```mdx
<Component
  prop={  value  }
/>
```

Or with line breaks:

```mdx
<Component
  prop={
    value
  }
/>
```

The whitespace inside the JSX expression braces doesn't seem to be processed correctly. The parser appears to exit the whitespace state prematurely or return to the wrong state after encountering certain whitespace patterns.

### Expected behavior

Whitespace inside JSX expressions should be handled correctly, allowing for proper formatting and multiple spaces/line breaks without causing parsing issues. The parser should correctly transition between whitespace states and maintain proper token boundaries.

### Additional context

This seems to affect specifically the handling of whitespace within JSX attribute values and expressions. Regular JSX content outside of expressions appears to work fine.

---
Repository: /testbed
