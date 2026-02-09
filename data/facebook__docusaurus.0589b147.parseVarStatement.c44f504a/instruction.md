# Bug Report

### Describe the bug

I'm encountering an issue with variable declarations in MDX files. It seems like the parser is handling variable statements incorrectly, causing semicolons to be inserted before the variable is actually parsed.

### Reproduction

When I try to use variable declarations in my MDX content, the parsing behavior is broken:

```mdx
export const myVar = 'test';

<Component value={myVar} />
```

The parser appears to be calling `semicolon()` before `parseVar()`, which means the variable declaration isn't being properly processed before the statement is considered complete. This leads to unexpected parsing errors or incorrect AST generation.

### Expected behavior

Variable declarations should be fully parsed before the semicolon is processed. The parser should:
1. Move to the next token
2. Parse the variable declaration completely
3. Then handle the semicolon

This order ensures the variable is properly registered in the AST before the statement is finalized.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest LTS

---
Repository: /testbed
