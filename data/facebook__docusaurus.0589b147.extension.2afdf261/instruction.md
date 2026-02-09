# Bug Report

### Describe the bug

I'm experiencing an issue with MDX extension handling where multiple extensions are not being merged correctly. When I register multiple extensions that define the same handlers (like `enter` or `exit`), only the last extension's handlers are being used instead of combining them properly.

### Reproduction

```js
const extension1 = {
  enter: {
    heading: (token) => console.log('Extension 1: heading'),
  },
  canContainEols: ['emphasis', 'strong']
}

const extension2 = {
  enter: {
    paragraph: (token) => console.log('Extension 2: paragraph'),
  },
  canContainEols: ['link']
}

// Register both extensions
// Expected: Both enter handlers should be available
// Actual: Only extension2's handlers are present
```

### Expected behavior

When combining multiple extensions:
- Handler objects (`enter`, `exit`) should merge all handlers from both extensions
- Array properties like `canContainEols` should preserve elements from all extensions in the correct order

Currently it seems like the second extension is completely overwriting the first one instead of merging with it.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This is blocking me from using multiple plugins that need to register handlers for the same event types. Any help would be appreciated!

---
Repository: /testbed
