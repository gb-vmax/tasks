# Bug Report

### Describe the bug

Sidebars are not loading when the sidebars file exists. After a recent update, my documentation site stopped displaying the sidebar navigation completely. The sidebar configuration file is present and valid, but it's being treated as if it doesn't exist.

### Reproduction

1. Create a docs plugin with a valid `sidebars.js` file
2. Add some sidebar configuration:
```js
module.exports = {
  docs: [
    'intro',
    'getting-started',
    {
      type: 'category',
      label: 'Guides',
      items: ['guide1', 'guide2']
    }
  ]
}
```
3. Start the dev server
4. The sidebar doesn't appear - no navigation is rendered

### Expected behavior

The sidebar should load and display the configured navigation structure when a valid sidebars file exists.

### System Info

- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

This was working fine before, but after pulling the latest changes the sidebars stopped loading entirely. The file is definitely there and the configuration looks correct.

---
Repository: /testbed
