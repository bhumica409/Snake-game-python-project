def gameLoop():
    while True:
        game_over = False
        game_close = False

        x1, y1 = width // 2, height // 2
        x1_change, y1_change = 0, 0
        snake_list = []
        length_of_snake = 1
        foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and x1_change == 0:
                        x1_change, y1_change = -snake_block, 0
                    elif event.key == pygame.K_RIGHT and x1_change == 0:
                        x1_change, y1_change = snake_block, 0
                    elif event.key == pygame.K_UP and y1_change == 0:
                        x1_change, y1_change = 0, -snake_block
                    elif event.key == pygame.K_DOWN and y1_change == 0:
                        x1_change, y1_change = 0, snake_block

            if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
                game_close = True

            x1 += x1_change
            y1 += y1_change
            display.fill(blue)
            pygame.draw.rect(display, green, [foodx, foody, snake_block, snake_block])
            
            snake_head = [x1, y1]
            snake_list.append(snake_head)
            if len(snake_list) > length_of_snake:
                del snake_list[0]

            if snake_head in snake_list[:-1]:
                game_close = True

            our_snake(snake_block, snake_list)
            score = length_of_snake - 1
            value = score_font.render("Score: " + str(score), True, white)
            display.blit(value, [0, 0])
            pygame.display.update()

            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
                length_of_snake += 1

            clock.tick(snake_speed)

        while game_close:
            display.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        game_close = False
                        game_over = False
                        break
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        return