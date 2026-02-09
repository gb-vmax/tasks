# Bug Report

### Describe the bug

I'm encountering an issue where JavaScript keywords are not being recognized properly in MDX files. It seems like the parser is failing to identify reserved words like `if`, `else`, `for`, `function`, etc. and is treating them as regular identifiers instead.

### Reproduction

```mdx
export const Example = () => {
  if (true) {
    return <div>Hello</div>
  }
}
```

When parsing this MDX content, the `if` keyword is not being recognized correctly and causes unexpected parsing behavior. The parser appears to be checking against an undefined value instead of the actual word being parsed.

### Expected behavior

JavaScript keywords should be properly identified and tokenized as keywords rather than generic names/identifiers. The parser should correctly distinguish between reserved words and regular variable names.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This seems to have started happening recently. Any help would be appreciated!

---
Repository: /testbed
