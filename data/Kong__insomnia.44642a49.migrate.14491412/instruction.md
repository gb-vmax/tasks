# Bug Report

### Describe the bug

After a recent update, proto file models are getting corrupted when they go through the migration process. The application crashes with a JSON parsing error when trying to load existing proto files.

### Reproduction

1. Create a proto file in the workspace
2. Restart the application or trigger a migration
3. Application crashes when attempting to parse the proto file

The issue seems to be related to how proto files are being migrated. When the migration function runs, it's trying to parse the proto file object as JSON which causes the entire model to become unusable.

### Expected behavior

Proto files should migrate successfully without corruption. The migration process should preserve the existing proto file structure and data without attempting to parse objects as JSON strings.

### System Info
- Insomnia version: latest
- OS: Windows/Mac/Linux

---
Repository: /testbed
