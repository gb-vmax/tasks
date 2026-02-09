# Bug Report

### Describe the bug

I'm seeing unexpected behavior with version banners in the docs plugin. The current/latest version is now showing a banner when it shouldn't, and older versions are not displaying banners when they should.

### Reproduction

Set up a docs site with multiple versions:
- versions: ['2.0.0', '1.5.0', '1.0.0']
- latest version: 2.0.0

Current behavior:
- Version 2.0.0 (current) - shows no banner ❌ (should show no banner ✓)
- Version 1.5.0 (old) - shows no banner ❌ (should show a banner)
- Version 1.0.0 (old) - shows no banner ❌ (should show a banner)

The logic seems inverted - banners are appearing/not appearing on the wrong versions.

### Expected behavior

- The current/latest version should not display any version banner
- Older versions should display an appropriate banner indicating they are outdated
- Unreleased/upcoming versions should show an "unreleased" banner

### System Info

- Docusaurus version: latest
- Plugin: @docusaurus/plugin-content-docs

---
Repository: /testbed
