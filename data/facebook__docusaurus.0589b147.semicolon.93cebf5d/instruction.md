# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where valid JavaScript/JSX syntax is being rejected with unexpected token errors. It seems like the parser is incorrectly throwing errors for code that should be valid.

### Reproduction

```mdx
export const MyComponent = () => {
  return <div>Hello</div>
}

<MyComponent />
```

When parsing this MDX file, I get an "unexpected token" error even though the syntax appears to be correct. The error occurs during the parsing phase.

### Expected behavior

The MDX parser should correctly parse valid JavaScript expressions and JSX components without throwing unexpected token errors. Semicolons should be handled properly according to JavaScript's automatic semicolon insertion (ASI) rules.

### Additional context

This seems to be related to how the parser handles semicolons in certain contexts. The issue appeared recently and is blocking our ability to parse previously working MDX files.

---
Repository: /testbed
