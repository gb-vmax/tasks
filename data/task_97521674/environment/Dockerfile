FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with
mkdir -p /home/user/projects/translation_logs

cat > /home/user/projects/translation_logs/update_20240612.log <<'EOF'
2024-06-12 09:32:18 | locale:fr | key:homepage.header.title | status:updated | details:Translation updated for new campaign
2024-06-12 09:32:18 | locale:es | key:homepage.header.title | status:added | details:New translation provided
2024-06-12 09:35:02 | locale:de | key:account.email.body | status:failed | details:Plural form missing
2024-06-12 09:36:44 | locale:fr | key:footer.contact | status:added | details:Contact info added
2024-06-12 09:38:12 | locale:it | key:footer.contact | status:updated | details:Grammar fixed
2024-06-12 10:02:11 | locale:fr | key:homepage.header.subtitle | status:failed | details:Missing variable in string
2024-06-12 10:18:50 | locale:de | key:homepage.header.title | status:updated | details:Minor spelling correction
2024-06-12 10:21:53 | locale:es | key:settings.privacy | status:updated | details:Translation improved
2024-06-12 10:23:15 | locale:fr | key:settings.privacy | status:failed | details:Formatting tags invalid
2024-06-12 10:25:22 | locale:pt | key:homepage.header.subtitle | status:added | details:New addition for PT
2024-06-12 10:31:55 | locale:de | key:footer.contact | status:updated | details:Formality level checked
2024-06-12 11:04:22 | locale:fr | key:dashboard.welcome | status:failed | details:Variable mismatch
EOF

# Do NOT create filtered_update_20240612.log

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
