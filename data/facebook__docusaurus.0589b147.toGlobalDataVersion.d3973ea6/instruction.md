# Bug Report

### Describe the bug

When using the docs plugin with draft documents, the draft documents are appearing in the global data's `docs` array even though they should be filtered out. This causes draft content to be exposed in places where it shouldn't be visible.

### Reproduction

```js
// Setup a version with both regular docs and drafts
const version = {
  versionName: '1.0.0',
  docs: [
    { id: 'doc1', title: 'Regular Doc' },
    { id: 'doc2', title: 'Another Regular Doc' },
    { id: 'draft1', title: 'Draft Doc' }
  ],
  drafts: [
    { id: 'draft1', title: 'Draft Doc' }
  ],
  // ... other version properties
}

const globalData = toGlobalDataVersion(version)

// Expected: globalData.docs should only contain doc1 and doc2
// Actual: globalData.docs contains all three documents including draft1
console.log(globalData.docs) // Contains draft1 even though it's marked as draft
```

### Expected behavior

Draft documents should be excluded from the `docs` array in the global data. Only non-draft documents should appear in `globalData.docs`, while draft IDs should only be present in the `draftIds` array.

### System Info

- Docusaurus version: latest
- Plugin: @docusaurus/plugin-content-docs

---
Repository: /testbed
