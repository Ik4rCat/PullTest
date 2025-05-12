from github import Github

# 1. Аутентификация в GitHub (используйте токен из Settings > Developer Settings > Personal Access Tokens)
GITHUB_TOKEN = "ваш_github_токен"
g = Github(GITHUB_TOKEN)

# 2. Создание репозитория
user = g.get_user()
repo_name = "test-repo-for-pr"
repo = user.create_repo(repo_name, private=False, description="Тестовый репозиторий для PR")

file = repo.get_contents("main.py", ref=source_branch)
repo.update_file("main.py", "Add multiply function", new_contents, file.sha, branch=source_branch)

# 6. Создание Pull Request
pr_title = "Добавлена функция multiply"
pr_body = "Это тестовый PR для задания по Code Review. Проверьте, пожалуйста!"
pr = repo.create_pull(title=pr_title, body=pr_body, head=source_branch, base="main")

print(f"Pull Request создан: {pr.html_url}")