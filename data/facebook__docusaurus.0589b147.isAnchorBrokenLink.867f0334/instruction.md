# Bug Report

### Describe the bug

Links with anchors to non-existent pages are not being reported as broken links anymore. When a link points to a page that doesn't exist (like `/nonexistent#anchor`), the broken link checker is not flagging it as an error.

### Reproduction

Create a markdown file with a link to a non-existent page with an anchor:

```md
[Link to non-existent page](/this-page-does-not-exist#some-anchor)
```

Build the site - the broken link is not detected even though the target page doesn't exist.

### Expected behavior

Links to non-existent pages should be reported as broken links, regardless of whether they include an anchor hash or not. The broken link checker should catch `/nonexistent#anchor` just like it would catch `/nonexistent`.

This was working correctly before but seems to have regressed in recent versions.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
