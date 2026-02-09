# Bug Report

### Describe the bug

When using JSX fragments in classic mode, the fragment is being rendered twice. The output contains duplicate fragment content that shouldn't be there.

### Reproduction

```jsx
// Input JSX
<>
  <div>Hello</div>
  <span>World</span>
</>
```

When compiling with `jsx: 'classic'` mode, the fragment content appears duplicated in the output. It seems like the fragment is being rendered both in the classic mode handler and then falling through to render again.

### Expected behavior

The JSX fragment should only be rendered once in classic mode, producing the expected output without duplication.

### System Info
- Rollup version: latest
- JSX mode: classic

---
Repository: /testbed
