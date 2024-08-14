import requests
import os

def send_slack_notification(pr_author, pr_title, pr_url, reviewers):
    webhook_url = os.getenv("SLACK_WEBHOOK_URL")

    # Formatar a lista de revisores
    if not reviewers:
        reviewers = "(nenhum revisor designado)"
    else:
        reviewers = ', '.join(reviewers)

    # Mensagem a ser enviada ao Slack
    slack_data = {
        "text": f"PR aberto por *{pr_author}*\n"
                f"Título: {pr_title}\n"
                f"URL: {pr_url}\n"
                f"Revisores: {reviewers}"
    }

    response = requests.post(
        webhook_url, json=slack_data,
        headers={'Content-Type': 'application/json'}
    )

    if response.status_code != 200:
        raise ValueError(
            f"Request to Slack returned an error {response.status_code}, "
            f"the response is:\n{response.text}"
        )

# Exemplo de uso da função
if __name__ == "__main__":
    # Exemplos de dados que podem ser extraídos do GitHub Actions
    pr_author = os.getenv("PR_AUTHOR")
    pr_title = os.getenv("PR_TITLE")
    pr_url = os.getenv("PR_URL")
    reviewers = os.getenv("PR_REVIEWERS")

    # Enviar notificação
    send_slack_notification(pr_author, pr_title, pr_url, reviewers)
