import pygame
import random
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)

# Função para gerar um novo ponto branco na tela
def generate_point():
    return (random.randint(0, WIDTH), random.randint(0, HEIGHT))

# Função principal do jogo
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Clicker Game")

    clock = pygame.time.Clock()

    game_duration = 30  # duração do jogo em segundos
    start_time = pygame.time.get_ticks()

    score = 0

    point = generate_point()  # inicializa a variável point antes do loop

    point_timer = 0
    point_delay = 1000  # intervalo de tempo entre a geração de pontos em milissegundos

    running = True
    while running:
        screen.fill((0, 0, 0))

        # Verifica eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Verifica se houve um clique do mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # clique do botão esquerdo
                    mouse_pos = pygame.mouse.get_pos()
                    if mouse_pos[0] >= point[0] - 10 and mouse_pos[0] <= point[0] + 10 and mouse_pos[1] >= point[1] - 10 and mouse_pos[1] <= point[1] + 10:
                        score += 1

        # Verifica se o tempo acabou
        if pygame.time.get_ticks() - start_time >= game_duration * 1000:
            running = False

        # Desenha um novo ponto branco se necessário
        if pygame.time.get_ticks() - point_timer >= point_delay:
            point = generate_point()
            point_timer = pygame.time.get_ticks()

        pygame.draw.circle(screen, WHITE, point, 10)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    print("O tempo acabou! Sua pontuação é:", score)

if __name__ == "__main__":
    main()
