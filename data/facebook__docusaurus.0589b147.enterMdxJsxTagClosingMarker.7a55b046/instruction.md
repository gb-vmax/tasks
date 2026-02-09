# Bug Report

### Describe the bug

I'm encountering an issue with nested JSX tags in MDX files. When I have a self-closing tag inside another JSX component, I'm getting an error about an unexpected closing slash, even though the syntax is valid.

### Reproduction

```mdx
<Wrapper>
  <SelfClosing />
</Wrapper>
```

This throws an error:
```
Unexpected closing slash `/` in tag, expected an open tag first
```

The error occurs when parsing the self-closing tag (`<SelfClosing />`) that's nested inside the `<Wrapper>` component. This should be valid MDX syntax but it's being rejected.

### Expected behavior

Nested self-closing JSX tags should parse correctly without throwing errors. The above MDX should be valid and compile successfully.

### Additional context

This seems to be related to how the parser tracks the tag stack when encountering closing markers. Simple self-closing tags at the root level work fine, but nesting them inside other components triggers this error.

---
Repository: /testbed
