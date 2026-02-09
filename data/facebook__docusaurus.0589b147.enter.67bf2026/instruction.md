# Bug Report

### Describe the bug

I'm encountering an issue where JSX pragma comments in MDX files are not being parsed correctly. When I include pragma comments like `@jsxRuntime`, `@jsx`, or `@jsxFrag` at the top of my MDX file, they seem to be ignored or skipped.

### Reproduction

```mdx
{/* @jsxRuntime automatic */}
{/* @jsxImportSource preact */}

# My Component

<MyCustomComponent />
```

The pragma comments should be detected and used to configure the JSX runtime, but it appears they're being skipped during parsing. This causes the wrong JSX transform to be applied or the pragmas to not take effect at all.

### Expected behavior

The pragma comments should be properly parsed and used to configure the JSX runtime settings. When `@jsxRuntime automatic` is specified, it should use the automatic JSX transform. When `@jsxImportSource` is provided, it should import from the specified source.

### Additional context

This seems to affect the first pragma comment in particular - it's like the parser is starting from the wrong position when iterating through comments. Other comments after the first one appear to work fine.

---
Repository: /testbed
