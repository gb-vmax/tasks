FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/translations

cat > /home/user/translations/export.tsv << 'EOF'
string_id	context	source_en	translation_fr
btn_save	Used on all form footers	Save	Enregistrer
btn_cancel	Used on all form footers	Cancel	Annuler
msg_welcome	Shown on login page	Welcome back!	Bon retour !
err_not_found	HTTP 404 page	Page not found	Page introuvable
lbl_username	Login form label	Username	Nom d'utilisateur
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
