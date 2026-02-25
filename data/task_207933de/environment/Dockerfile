FROM ubuntu:22.04

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN <<'ENDPOST'
set -e

    # Install Python and pip
    apt-get update
    apt-get install -y python3 python3-pip

    # Install pytest
    pip3 install pytest

    # Create necessary directories
    mkdir -p /home/user/projects/localization/update_logs
    mkdir -p /home/user/projects/localization/update_reports

    # Set permissions so that the user (non-root) can read/write as needed
    chmod 755 /home/user
    chmod -R 755 /home/user/projects
    chmod -R 755 /home/user/projects/localization
    chmod -R 755 /home/user/projects/localization/update_logs
    chmod -R 777 /home/user/projects/localization/update_reports

    # Create the log file with the required content
    cat << EOF > /home/user/projects/localization/update_logs/translations_update.log
2024-06-11T15:34:12Z de button_submit MISSING
2024-06-11T15:34:12Z de menu_help PARTIAL
2024-06-11T15:34:12Z de about_title DONE
2024-06-11T15:34:12Z fr login_title MISSING
2024-06-11T15:34:12Z fr logout_success PARTIAL
2024-06-11T15:34:12Z fr profile_label DONE
2024-06-11T15:34:12Z fr menu_help PARTIAL
2024-06-11T15:34:12Z it menu_help PARTIAL
2024-06-11T15:34:12Z it logout_success DONE
2024-06-11T15:34:12Z it settings_label MISSING
2024-06-11T15:34:12Z de menu_help PARTIAL   # Duplicate; should be ignored in report
2024-06-11T15:34:12Z fr logout_success PARTIAL   # Duplicate; should be ignored
EOF

    # Ensure the log file is readable
    chmod 644 /home/user/projects/localization/update_logs/translations_update.log
ENDPOST

WORKDIR /home/user
