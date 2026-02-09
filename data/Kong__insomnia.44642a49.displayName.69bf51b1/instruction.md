# Bug Report

### Describe the bug

After a recent update, the template tag display names for request attributes are showing incorrectly. Previously, attributes like `oauth2`, `oauth2-identity`, `oauth2-refresh`, `name`, `folder`, and `url` would display as just "Name", but now they're showing formatted versions like "Oauth2 Name", "Oauth2 Identity Name", etc.

### Reproduction

When using the request template tag with these attribute types:
- `oauth2` now displays as "Oauth2 Name" instead of "Name"
- `oauth2-identity` now displays as "Oauth2 Identity Name" instead of "Name"
- `oauth2-refresh` now displays as "Oauth2 Refresh Name" instead of "Name"
- `name` now displays as "Request Name" instead of "Name"
- `folder` now displays as "Folder Name" instead of "Name"
- `url` now displays as "URL" instead of "Name"

### Expected behavior

These attribute types should all display as "Name" in the UI, just like before. Only `cookie`, `parameter`, and `header` should have custom display names ("Cookie Name", "Query Parameter Name", and "Header Name" respectively).

### Additional context

This appears to have changed in the template tag configuration for the request attribute selector. The display logic seems to have been modified to add formatted labels for attribute types that previously just showed "Name".

---
Repository: /testbed
