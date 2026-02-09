# Bug Report

### Describe the bug

I'm encountering an issue with MDX ESM data handling where the parser seems to be calling the wrong method during token exit. When processing MDX ESM blocks, the data is not being properly finalized, which causes the parsed output to be incorrect or incomplete.

### Reproduction

```js
const mdx = `
---
export const metadata = { title: 'Test' }
---

# Hello World
`

// Parse the MDX content
const result = compile(mdx)
// The ESM export is not properly processed
```

### Expected behavior

The ESM data block should be correctly parsed and the `exit.data` handler should be called with the proper token to finalize the data processing. Currently it appears the wrong context or parameters are being passed during the exit phase.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
