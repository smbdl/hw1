consonant = "qwrtypsdfghjklzxcvbnmйцкнгшщзхъфвпрлджчсмтьбю"
vowel = "euioaуеыаоэяию"
while True:
    c = 0
    v = 0
    word = input("\nCлово: ").upper().lower()
    if word == "stop" or word == "стоп":
        print("bye/пока")
        break
    print("Количество букв:", len(word))
    for i in word:
        if i in consonant:
            c += 1
    print("Согласных букв:", c)
    for i in word:
        if i in vowel:
            v += 1
    print("Гласных букв:", v)
    print(f"Гласные/Согласные: {round(v * 100 / len(word), 2)}% / {round(c * 100 / len(word), 2)}%")

    # consonant = 'qwrtyplkjhgfdszxcvbnmйцкнгшщзхъждлрпвфячсмтьбю'
    # vowel = 'euioaуеэоаыяию'
    # while True:
    #     word = input('word: ').lower()
    #     c = 0
    #     v = 0
    #     if word == 'stop':
    #         print('stop')
    #         break
    #     for i in word:
    #         if i in consonant:
    #             c += 1
    #     for i in word:
    #         if i in vowel:
    #             v += 1
    #     print(f'letters: {len(word)}\n'
    #           f'consonants: {c}\n'
    #           f'vowels: {v}\n'
    #           f'percentage: {round(v * 100 / len(word), 2)}% / {round(c * 100 / len(word), 2)}%')
