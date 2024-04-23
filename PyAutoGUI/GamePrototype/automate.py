import pyautogui
import time

# Função para encontrar a posição do ponto branco na tela
def find_white_point():
    # Encontre a posição do primeiro pixel branco na tela
    screen_shot = pyautogui.screenshot()
    for x in range(screen_shot.width):
        for y in range(screen_shot.height):
            if screen_shot.getpixel((x, y)) == (255, 255, 255):
                return (x, y)
    return None

# Função principal do script de automação
def auto_play_game():
    game_duration = 30  # duração do jogo em segundos
    start_time = time.time()

    score = 0

    while time.time() - start_time < game_duration:
        # Encontre a posição do ponto branco na tela
        white_point = find_white_point()
        if white_point:
            # Clique no ponto branco
            pyautogui.click(white_point)
            score += 1
            print("Clicou no ponto branco!")
        else:
            print("Não encontrou o ponto branco!")

        # Aguarde um curto período de tempo antes de procurar novamente
        time.sleep(0.1)

    print("O tempo acabou! Sua pontuação é:", score)

if __name__ == "__main__":
    auto_play_game()
