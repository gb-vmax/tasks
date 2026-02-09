# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where variable declarations are being incorrectly parsed. The parser seems to be processing variable statements in the wrong order and also appears to be mislabeling the node type.

### Reproduction

When parsing MDX files that contain variable declarations, the parser is not handling them correctly. Here's what I'm seeing:

```mdx
export const myVariable = 'test';
```

The variable statement gets parsed but the AST node structure appears incorrect. The parser seems to be calling methods in an unexpected sequence.

### Expected behavior

Variable declarations should be parsed correctly with:
1. Proper sequencing of parsing operations
2. Correct node type in the AST (should be "VariableDeclaration" not something else)
3. Tokens consumed in the right order

### System Info
- remark-mdx version: 3.0.0
- Using the vendored version in Jest

This might be affecting MDX files that use export statements with variable declarations. Any help would be appreciated!

---
Repository: /testbed
