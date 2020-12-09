def solution(board, moves):
    answer = 0
    basket = []
                
    for _ in range(len(moves)):
        row = moves.pop(0)
        for i in range(len(board)):
            if board[i][row-1] != 0:
                if len(basket) > 0 and (basket[len(basket)-1] == board[i][row-1]):
                    basket.pop()
                    answer += 2
                else:
                    basket.append(board[i][row-1])
                    
                board[i][row-1] = 0
                break

    return answer