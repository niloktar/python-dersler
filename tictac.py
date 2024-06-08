#tic tac toe game 
print("SOS Oyunumuza hoş geldin!")

board = [' ' for x in range(12)]
def oyun_tahtasi():
    satir1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    satir2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    satir3 = "| {} | {} | {} |".format(board[6], board[7], board[8])
    satir4 = "| {} | {} | {} |".format(board[9], board[10], board[11])

    print("--------------")
    print(satir1)
    print(satir2)
    print(satir3)
    print(satir4)
    print('--------------')
#Oyuna başlıyoruz
def oyuncu_hamlesi(icon):
    if icon == 'S':
        oyuncu = 1 #oyuncu 1 "S" yazacak
    elif icon == 'O':
        oyuncu = 2 #Oyuncu 2 "O" yazacak
    print("Sıra sende Oyuncu {}".format(oyuncu))
    #Aynı yeri seçmek için 3 yanlış hamle hakkımız var. 
    deneme = 0
    max_deneme = 3
    # Deneme sayımız toplam hakkımızdan küçük olduğu durumda oyun devam eder.
    while deneme < max_deneme:
        hamle = int(input("Hamleni yapacağın yeri seç (1-9): ").strip())
        if board[hamle - 1] == ' ':
            board[hamle - 1] = icon
            break
        else: 
            print()
            print("Burası dolu!")
            deneme += 1 #her aynı hamlede deneme hakkımıza bir tane eklenir.
    # Deneme sayımız toplam hakkımızdan eşit olduğu durumda oyundan atar.
    if deneme == max_deneme: 
        print("Çok fazla deneme yaptın! Oyun şimdi kapanıyor.")
        sys.exit()
        
def is_victory(icon): #Kazanma olasılıkları, yanyana ya da çapraz ise kazandı.
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board[5] == icon) or \
       (board[6] == icon and board[7] == icon and board[8] == icon) or \
       (board[0] == icon and board[3] == icon and board[6] == icon) or \
       (board[1] == icon and board[4] == icon and board[7] == icon) or \
       (board[2] == icon and board[5] == icon and board[8] == icon) or \
       (board[0] == icon and board[4] == icon and board[8] == icon) or \
       (board[3] == icon and board[7] == icon and board[11] == icon) or \
       (board[3] == icon and board[6] == icon and board[9] == icon) or \
       (board[5] == icon and board[7] == icon and board[9] == icon) or \
       (board[4] == icon and board[7] == icon and board[10] == icon) or \
       (board[5] == icon and board[8] == icon and board[11] == icon) or \
       (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False

def is_draw():
    if ' ' not in board: #seçtiğimiz sayı tabloda yok ise;
        return True
    else:
        return False #Oyunu durdur.

while True:
    oyun_tahtasi()
    oyuncu_hamlesi('S')
    oyun_tahtasi()
    if is_victory('S'):
        print("Oyuncu 1 Kazandı! Tebrikler!")
        break
    elif is_draw():
        print("İşte bu! Kazandın!")
        break
    oyuncu_hamlesi('O')
    if is_victory('O'):
        oyun_tahtasi()
        print("Oyuncu 2 kazandı! Tebrikler! ")
        break
    elif is_draw():
        print("İşte bu! Kazandın!")
        break
