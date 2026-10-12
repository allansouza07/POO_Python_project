

def escolha():
    while True:
        try: 
            escolha = int(input("Escolha um desses restaurantes para observar seu cardápio: \n" \
            "1)Restaurante do bahiano\n2)Restaurante natural\n3)Burguer Restaurante\n- "))
        except ValueError:
            print("Erro! Número inválido")
            continue
        else:
            return escolha

escolha_usuario = escolha()

def main(escolha):
    if escolha == 1:
        from modelos.restaurantes import restaurante_bahiano
        restaurante_bahiano.listar_cardapio
    elif escolha ==2:
        from modelos.restaurantes import  restaurante_natural
        restaurante_natural.listar_cardapio
    elif escolha ==3:
        from modelos.restaurantes import  burguer_restaurante
        burguer_restaurante.listar_cardapio
    else:
        print("Erro!")

if __name__ == '__main__':
    main(escolha_usuario)

print("\nObrigado!")