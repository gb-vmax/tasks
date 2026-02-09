# Bug Report

### Describe the bug

After a recent update, the docs sidebar configuration is broken. When navigating through documentation pages, I'm getting errors about accessing sidebar properties. It looks like the docs metadata is not being generated correctly.

### Reproduction

```js
// In a Docusaurus project with multiple docs
const docsMetadata = {
  docs: [
    { id: 'intro', title: 'Introduction', sidebar: 'tutorialSidebar' },
    { id: 'getting-started', title: 'Getting Started', sidebar: 'tutorialSidebar' }
  ]
}

// Try to access a specific doc by its ID
const doc = docsMetadata['intro']
// doc is undefined - can't find the document by ID anymore
```

### Expected behavior

Documents should be accessible by their ID in the version docs prop. The sidebar property should also be correctly assigned to each individual document, not trying to access a property on the entire docs array.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This is blocking our documentation site from building correctly. The docs are indexed by numeric indices instead of their document IDs, and the sidebar property assignment looks wrong.

---
Repository: /testbed
