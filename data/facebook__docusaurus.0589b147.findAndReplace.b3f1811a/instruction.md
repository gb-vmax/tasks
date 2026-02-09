# Bug Report

### Describe the bug

I'm experiencing an issue with the remark-gfm plugin where text replacement operations seem to be skipping content or not processing all matches correctly. When using find-and-replace functionality on markdown content, some replacements are being missed or the traversal appears to be jumping over nodes.

### Reproduction

```js
const tree = {
  type: 'root',
  children: [
    { type: 'text', value: 'foo bar foo' },
    { type: 'text', value: 'baz foo qux' }
  ]
}

// Attempting to replace all instances of 'foo'
findAndReplace(tree, [['foo', 'replaced']])

// Expected: all 'foo' instances replaced
// Actual: some 'foo' instances are skipped
```

### Expected behavior

All matching text patterns should be found and replaced during tree traversal. The plugin should process each node sequentially without skipping any matches.

### System Info
- remark-gfm version: 4.0.0
- Node version: 18.x

This seems to have broken recently and is affecting markdown processing in our documentation pipeline. Any help would be appreciated!

---
Repository: /testbed
