word = input("Inserte una palabra: \n")
word1 = list(word)
print("Es palindromo") if word1 == list(reversed(word1)) else print("No es palindromo")