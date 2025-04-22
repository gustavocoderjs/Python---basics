
import requests

def obter_posts():
    # URL da API JSONPlaceholder para obter posts
    url = 'https://jsonplaceholder.typicode.com/posts'
    
    try:
        # Fazer a solicitação GET para a API
        resposta = requests.get(url)
        resposta.raise_for_status()  # Levanta um erro se a solicitação falhar
        
        # Converter a resposta para JSON
        posts = resposta.json()
        
        return posts
    
    except requests.exceptions.RequestException as e:
        # Imprimir erros se houver problemas na solicitação
        print(f'Erro ao fazer a solicitação: {e}')
        return None

def exibir_posts(posts):
    if posts:
        # Exibir os primeiros 5 posts para simplificar
        for post in posts[:5]:
            print(f"ID: {post['id']}")
            print(f"Título: {post['title']}")
            print(f"Corpo: {post['body']}\n")
    else:
        print('Nenhum post encontrado.')

def main():
    posts = obter_posts()
    exibir_posts(posts)

if __name__ == '__main__':
    main()
