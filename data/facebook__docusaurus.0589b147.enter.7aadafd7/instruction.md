# Bug Report

### Describe the bug

I'm encountering an issue where JSX pragma comments at the beginning of MDX files are being skipped and not processed correctly. When I have a `@jsxRuntime` or other JSX-related pragma in the first comment of my file, it's completely ignored, but comments after the first one work fine.

### Reproduction

```mdx
/* @jsxRuntime classic */
/* @jsx React.createElement */

export default function MyComponent() {
  return <div>Hello</div>
}
```

The first comment with `@jsxRuntime classic` is not being parsed, so the runtime defaults to automatic mode instead of using the specified classic runtime. If I add a dummy comment before it, then it works:

```mdx
/* dummy comment */
/* @jsxRuntime classic */
/* @jsx React.createElement */

export default function MyComponent() {
  return <div>Hello</div>
}
```

This workaround shouldn't be necessary.

### Expected behavior

The first comment in the file should be processed for JSX pragmas just like any other comment. The `@jsxRuntime`, `@jsx`, `@jsxFrag`, and `@jsxImportSource` annotations should be recognized regardless of their position in the comments array.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
