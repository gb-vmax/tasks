# Bug Report

### Describe the bug

The order of documents in the global data has changed unexpectedly. When accessing the docs array in a version, the category generated indices now appear before regular docs instead of after them. This is affecting the order in which documents are displayed/processed.

### Reproduction

```js
// When accessing version data
const version = getVersionData();
console.log(version.docs);

// Expected: regular docs first, then generated indices
// Actual: generated indices first, then regular docs
```

Steps to reproduce:
1. Set up a docs plugin with multiple documents and category generated indices
2. Access the global data for a version
3. Check the order of items in the `docs` array
4. Notice that generated indices appear first instead of last

### Expected behavior

The `docs` array should contain regular documentation pages first, followed by category generated index pages at the end. This was the previous behavior and changing the order breaks assumptions about document ordering.

### Additional context

Also noticed that `draftIds` is now pulling from `version.docs` instead of `version.drafts` which seems incorrect - it should only include actual draft documents, not all documents.

---
Repository: /testbed
