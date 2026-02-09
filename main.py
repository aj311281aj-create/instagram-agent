"""
Instagram Agent - Script principal
"""

from instagram_agent import InstagramAgent
import schedule
import time

def main():
    # Inicializar o agente
    agent = InstagramAgent()
    
    # Fazer login
    if not agent.login():
        print("Falha ao fazer login. Verifique suas credenciais.")
        return
    
    # Exemplos de uso
    print("\n=== Instagram Agent iniciado ===\n")
    
    # Obter informações do usuário
    user_info = agent.get_user_info(agent.username)
    if user_info:
        print(f"👤 Usuário: {user_info.full_name}")
        print(f"📊 Seguidores: {user_info.follower_count}")
        print(f"📝 Posts: {user_info.media_count}\n")
    
    # Você pode agendar tarefas aqui
    # schedule.every().day.at("10:00").do(agent.post_content, image_path="foto.jpg", caption="Novo post!")
    
    # Loop para executar tarefas agendadas
    # while True:
    #     schedule.run_pending()
    #     time.sleep(60)
    
    # Fazer logout ao finalizar
    agent.logout()

if __name__ == "__main__":
    main()