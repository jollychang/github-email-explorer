from github_email_explorer import github_email

ges = github_email.collect_email_info('yuecen', 'github-email-explorer', ['star', 'watch'])

# With Authentication
# github_api_auth = ('<your_client_id>', '<your_client_secret>')
# ges = github_email.collect_email_info('yuecen', 'github-email-explorer', ['star', 'watch'],
#                                        github_api_auth=github_api_auth)

for ge in ges:
    print ge.g_id, "->", ge.name, ",", ge.email, ",", ge.location
