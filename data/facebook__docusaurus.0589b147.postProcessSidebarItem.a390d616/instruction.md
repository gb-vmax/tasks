# Bug Report

### Describe the bug

I'm experiencing an issue with the sidebar configuration where draft documents are appearing in the sidebar when they shouldn't be visible. It seems like the draft filtering logic is inverted - draft items are being shown instead of being hidden.

### Reproduction

1. Create a document and mark it as draft in the frontmatter:
```md
---
draft: true
---
# My Draft Document
```

2. Add this document to your sidebar configuration:
```js
{
  type: 'doc',
  id: 'my-draft-doc',
  label: 'My Draft'
}
```

3. Build or serve the documentation

### Expected behavior

Draft documents should be filtered out and not appear in the sidebar. Only published documents should be visible to users.

### Actual behavior

Draft documents are showing up in the sidebar as if they were published. Non-draft documents are being filtered out instead.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This is causing draft content to be exposed in production builds which is a pretty serious issue. Any help would be appreciated!

---
Repository: /testbed
