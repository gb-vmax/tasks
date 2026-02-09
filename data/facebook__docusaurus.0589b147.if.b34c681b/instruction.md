# Bug Report

### Describe the bug

Sidebars are not loading in my Docusaurus site. When I start the dev server, all pages show up without any sidebar navigation, even though I have a valid `sidebars.js` file configured.

### Reproduction

1. Create a Docusaurus project with a `sidebars.js` file
2. Add some sidebar configuration:
```js
module.exports = {
  docs: [
    'intro',
    {
      type: 'category',
      label: 'Tutorial',
      items: ['tutorial-basics/create-a-page'],
    },
  ],
};
```
3. Start the dev server
4. Navigate to any docs page

### Expected behavior

The sidebar should be visible and display the configured navigation structure from `sidebars.js`.

### Actual behavior

No sidebar appears on any page. The pages render but the sidebar navigation is completely missing.

### System Info

- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

This just started happening after pulling the latest changes. My sidebars configuration hasn't changed and was working fine before.

---
Repository: /testbed
