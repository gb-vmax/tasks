# Bug Report

### Describe the bug

I'm experiencing an issue with exporting requests where certain workspace descendants are not being included in the export. It seems like WebSocket payloads and some other resource types are being filtered out incorrectly.

### Reproduction

1. Create a workspace with the following items:
   - A few requests
   - Environment configurations
   - WebSocket payloads
   - Proto files/directories
2. Attempt to export the workspace data using `exportRequestsData()`
3. Check the exported resources

### Expected behavior

All descendants of the workspace should be included in the export, specifically:
- Cookie jars
- Environments
- API specs
- Unit test suites
- Unit tests
- Proto files
- Proto directories
- WebSocket payloads

### Actual behavior

WebSocket payloads (and possibly other resources) are missing from the exported data. The filter logic appears to be excluding resources that should be included.

### Additional context

This seems to affect the `db.withDescendants()` filtering logic where workspace descendants are being collected. The exported file is missing resources that were previously included in exports.

---
Repository: /testbed
