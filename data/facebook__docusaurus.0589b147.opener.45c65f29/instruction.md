# Bug Report

### Bug with MDX parsing - incorrect token handling order

I've encountered an issue with MDX compilation where tokens are being processed in the wrong order, causing the parser to fail or produce incorrect output.

### Reproduction

When parsing MDX content with certain nested structures, the compiler seems to be calling functions with arguments in an unexpected order. This affects how tokens are entered into the processing stack.

```mdx
# Example content that triggers the issue

<Component>
  Some nested content here
</Component>
```

The issue appears to be related to how the opener function handles token creation and entry. The token object and the result of create4() are being passed in the wrong sequence, which breaks the internal processing.

### Expected behavior

The MDX content should parse correctly and tokens should be processed in the proper order. The `enter` function should receive the correct arguments so that the AST is built properly.

### Additional context

This seems to have broken recently. The compiler is now calling `enter` with swapped arguments, which causes downstream issues in the parsing pipeline. The token creation callback and the token itself need to be handled in the correct sequence.

---
Repository: /testbed
