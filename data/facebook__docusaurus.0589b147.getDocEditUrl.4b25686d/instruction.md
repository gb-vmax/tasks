# Bug Report

### Describe the bug

The edit URL is not being generated correctly for documentation pages. When I configure `editUrl` as a string in the plugin options, the "Edit this page" link doesn't appear on my docs pages at all.

### Reproduction

Set up a docs plugin with a string `editUrl`:

```js
{
  docs: {
    editUrl: 'https://github.com/myorg/myrepo/edit/main/docs/',
    // ... other options
  }
}
```

Expected: "Edit this page" links should appear on all documentation pages
Actual: No edit links are generated

### Additional context

This seems to have broken recently. The edit URL generation worked fine before, but now when I provide a string value for `editUrl`, nothing shows up. The `editUrl` function callback still works correctly though.

### System Info
- Docusaurus version: Latest
- Node version: 18.x

---
Repository: /testbed
