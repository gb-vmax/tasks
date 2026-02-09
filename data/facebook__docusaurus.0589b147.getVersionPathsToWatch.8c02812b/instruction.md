# Bug Report

### Describe the bug

The plugin is not correctly watching all file paths for changes. When I modify certain files in my docs directory, the development server doesn't pick up the changes and I have to manually restart it.

### Reproduction

1. Set up a Docusaurus project with the docs plugin
2. Configure multiple include patterns in the plugin options (e.g., `['**/*.md', '**/*.mdx']`)
3. Make changes to documentation files
4. Observe that some file changes are not being detected by the file watcher

The issue seems to be related to how the plugin constructs the list of paths to watch. It looks like the paths aren't being flattened correctly when there are multiple include patterns.

### Expected behavior

All files matching the include patterns should be watched for changes, and the development server should hot-reload when any of them are modified.

### System Info
- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
