def calculate_score(declaration):
    english_scores = {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
                      'D': 2, 'G': 2,
                      'B': 3, 'C': 3, 'M': 3, 'P': 3,
                      'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
                      'K': 5,
                      'J': 8, 'X': 8,
                      'Q': 10, 'Z': 10}

    russian_scores = {'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
                      'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
                      'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
                      'Й': 4, 'Ы': 4,
                      'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
                      'Ш': 8, 'Э': 8, 'Ю': 8,
                      'Ф': 10, 'Щ': 10, 'Ъ': 10}

    achieve = 0
    if declaration.isalpha():
        declaration = declaration.upper()
        if declaration[0] in english_scores:
            for letter in declaration:
                achieve += english_scores[letter]
        elif declaration[0] in russian_scores:
            for letter in declaration:
                achieve += russian_scores[letter]
        else:
            print("Неизвестный алфавит")
            return None
        return achieve
    else:
        print("Некорректное слово")
        return None


word = input("Введите слово: ")
score = calculate_score(word)
if score is not None:
    print("Стоймость слова:", score)

