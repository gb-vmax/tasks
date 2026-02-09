# Bug Report

### Describe the bug

The CLI command descriptions for versioning docs are swapped when using multiple plugin instances. The default plugin instance shows the description with the plugin ID suffix, while non-default instances show the generic description without the ID.

### Reproduction

1. Configure multiple docs plugin instances in `docusaurus.config.js`:
```js
plugins: [
  '@docusaurus/plugin-content-docs',
  [
    '@docusaurus/plugin-content-docs',
    {
      id: 'community',
      // ... other options
    },
  ],
]
```

2. Run `npx docusaurus --help` to view available commands

3. Observe the command descriptions:
   - `docs:version` shows: "Tag a new docs version (community)" (should be generic)
   - `docs:version:community` shows: "Tag a new docs version" (should include the plugin ID)

### Expected behavior

The command descriptions should be:
- `docs:version`: "Tag a new docs version" (generic description for default instance)
- `docs:version:community`: "Tag a new docs version (community)" (description with plugin ID for named instance)

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
