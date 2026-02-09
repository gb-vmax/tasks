# Bug Report

### Describe the bug

After updating to the latest version, the blog plugin translation keys seem to have changed. My custom translations are no longer being applied correctly - the sidebar title is showing the default value instead of my translated text, and the translation file path appears to have changed as well.

### Reproduction

1. Set up a Docusaurus site with the blog plugin
2. Create a custom translation file at `i18n/[locale]/docusaurus-plugin-content-blog/options.json`
3. Add custom translations for the sidebar:
```json
{
  "sidebar.title": {
    "message": "My Custom Sidebar Title"
  }
}
```
4. Build or run the site
5. The custom sidebar title doesn't appear - it shows the default instead

### Expected behavior

The translation file should be read from the `options.json` file and the `sidebar.title` key should apply my custom translation to the blog sidebar.

### System Info
- Docusaurus version: latest
- Node version: 18.x

It looks like the translation keys might have been renamed or the file structure changed? My existing translations worked fine in the previous version.

---
Repository: /testbed
