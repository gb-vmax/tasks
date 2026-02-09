# Bug Report

### Describe the bug

I'm experiencing an issue with the sync diff algorithm where it seems to be creating way more operations than necessary when comparing similar strings. The diff output is extremely verbose and contains a lot of redundant operations, making syncing really slow for large documents.

### Reproduction

When I try to sync documents that have minor changes, the diff algorithm appears to be generating excessive operations. For example:

```js
const oldValue = "This is a test document with some repeated content. " +
                 "This is a test document with some repeated content. " +
                 "This is a test document with some repeated content.";
                 
const newValue = "This is a test document with some modified content. " +
                 "This is a test document with some repeated content. " +
                 "This is a test document with some repeated content.";

// The diff between these should be minimal (just one word change)
// But it's generating tons of small operations instead
```

### Expected behavior

The diff algorithm should recognize that most of the content is identical and only generate operations for the actual changes. With just a single word modification, I'd expect maybe 1-3 operations, not dozens.

### System Info

- Insomnia version: latest
- OS: macOS

This is causing major performance issues when syncing larger workspaces. Any help would be appreciated!

---
Repository: /testbed
