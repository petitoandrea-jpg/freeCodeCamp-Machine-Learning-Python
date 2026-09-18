def player(prev_play, opponent_history=[], play_order={}):
    # Ripristina lo stato all'inizio di una nuova sfida
    if prev_play == "":
        opponent_history.clear()
        play_order.clear()

    if prev_play:
        opponent_history.append(prev_play)

    # Mossa predefinita per le prime partite
    guess = "R"

    # Sequenza di lunghezza n=5 basata sulle mosse dell'avversario
    n = 5

    if len(opponent_history) >= n:
        # Registra la sequenza corrente delle ultime n mosse
        pattern = "".join(opponent_history[-n:])
        play_order[pattern] = play_order.get(pattern, 0) + 1

        # Prepara la sottosequenza delle ultime n-1 mosse
        sub_order = "".join(opponent_history[-(n - 1):])

        # Costruisci le tre possibili evoluzioni
        potential_moves = [sub_order + "R", sub_order + "P", sub_order + "S"]

        # Prevedi quale mossa l'avversario giocherà più probabilmente
        prediction = max(potential_moves, key=lambda key: play_order.get(key, 0))[-1]

        # Rispondi battendo la mossa prevista
        ideal_response = {"R": "P", "P": "S", "S": "R"}
        guess = ideal_response[prediction]

    return guess